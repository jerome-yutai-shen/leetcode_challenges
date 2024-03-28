# -*- coding: utf-8 -*-
"""
Created on Nov 12 16:59:50 2023

@author: Jerome Yutai Shen

"""
"""
此题目跟Lintcode不同！

扫描线+前缀和精华版
这道题之所以被称为精华版， 是因为这个题目把2种算法用到了极致。

首先， 开一个范围那么大的数组， 然后对于每个interval， mark一下不available。 也就是用了+1没用-1.

然后， 其实可以另外开一个数组， 等等再常数级别优化， 这个时候， 我们有了整个所有time的占用情况， 这个时候知道每个时间， 占用了几个。

然后我们根据占用情况， 反推出可用情况， 就是占用跟总房间去比。

然后妙的来啦， 怎么样在常数时间， 知道每个ask行不行呢？这里我们直接把available的时间标成1， 不available标成0. 然后再去算一个前缀和。 

然后看一下前缀和和出来， 和区间长度比较， 如果区间里面都是1，那么加起来肯定等于区间长度。 那么这个题目答案就出来了
"""
"""
对Leetcode的题目分析

比较复杂的堆模拟问题。首先分析题目给的三个条件：

1、每场会议使用未被占用的编号最小的会议室。在这里就需要使用一个堆来维护当前没有被占用的会议室，这样一来就可以高效得到其中编号最小的会议室是哪一个

2、如果没有可用的会议室，那么会议将延期，直到有空闲会议室为止。会议延期，意味着还需要使用某种数据结构来维护延期的会议，具体的放在条件三来说明。
另外，会议的延期会一直到有空闲的会议室出现，这里的隐藏需求就是对于正在进行的会议，必须能高效地知道这些会议完结时间的最小值，因为最早空闲的会议室将提供给延期的会议使用。
因此在这里需要使用第二个，来维护正在进行的会议的完结时间以及会议室编号

3、当会议室空闲时，将提供给原定召开时间最早的会议。那么在这里则需要使用第三个堆，来维护延期会议的原定起始时间和原定结束时间。
在这里维护原定结束时间的理由时会议召开时需要通过原定的起始和结束时间计算会议具体需要花费的时间，用来更新2里面堆中维护的会议完结时间。当然，在这里也可以直接维护会议的起始时间和花费时间。


综合起来，就是三个堆idle，min_time和pending，具体作用如上所述。其中idle初始化为[0, 1, ..., n - 1]，即一开始所有会议室都是空闲的，而min_time和pending则初始化为空。

接下来将会议按起始时间从小到大排序，然后一趟遍历。对于当前遍历到的会议，不妨设其开始和结束时间分别为start_time和end_time，那么：

首先，若min_time不为空，且min_time[0][0]，也就是最早完结的会议的时间小于等于start_time，那么就应该先将这些会议室释放出来。
即将min_time的堆顶弹出，然后将其中对应的会议室编号重新加入到idle当中。
在这里需要注意的是，每当一个会议完结，若此时pending非空，说明有延期的会议在等会议室，那么就应该立即安排pending中原定时间最早的会议在刚空出来的会议室召开，召开的时间就是上一场会议完结的时间。

这里有一个隐藏条件是pending中的会议都是被迫延期的，即pending中的会议在其原计划召开的时刻是找不到空闲会议室的，而当前刚完结的会议其完结时间必然大于原计划召开的时间，否则的话这场会议就无须pending了。
也就是说，会议室空出来的时间总是大于原计划召开的时间，因此在这里召开的时间就必然是上一次会议完结的时间。
记刚完结的会议其完结时间为now，在会议室num召开，那么这里就应该立刻安排pending[0]表示的会议在now时刻，num会议室召开，此时应该将pending的堆顶弹出，记为meeting_info。
那么该会议的持续时间就是meeting_info[1] - meeting_info[0]，因此这场会议的完结时间就是now + meeting_info[1] - meeting_info[0]，将这个时间和会议室编号num加入到min_time中，并更新会议室num的使用次数。

接下来，若存在空闲的会议室，那么就用其中编号最小的来召开当前这场从start_time到end_time的会议，否则就将当前这场会议加入到pending中

遍历完成后，可能出现的一种情况是所有会议室都占满了，但还有会议在等待中，此时就需要等待正在进行的会议逐个完结，并在完结的时刻立即安排等待的会议召开。具体来说，就是当pending非空时：

若idle为空，即没有空闲的会议室，那么就需要等到所有正在进行的会议中结束时间最早的会议结束。记这个时间为now，那么当min_time的堆顶记录的时间恰好为now时，就将其弹出。
重复此过程直到min_time为空或者堆顶记录的时间大于now为止。

接下来，就必然有了至少一个空闲的会议室，那么将其安排给pending堆顶的会议即可。

注意到题目中多次出现将idle堆顶的会议室安排给pending堆顶的会议，那么在具体实现的时候可以将这个会议开始的行为抽象出来，更进一步的，对于可以正常召开的会议，也可以先将其加入到pending中再立马将其安排在idle堆顶的会议室。

所有的会议都召开之后，返回使用次数最多的会议室即可。
"""
from collections import defaultdict, deque
import heapq
from typing import List


def most_booked(n: int, meetings: List[List[int]]) -> int:
    meetings.sort(key=lambda x: x[0])
    idle_rooms = list(range(n - 1, 0, -1))
    taken_rooms = [[meetings[0][1], 0]]
    used_times = dict.fromkeys(range(n), 0)
    used_times[0] = 1
    for meeting in meetings[1:]:
        start, end = meeting
        while taken_rooms and start >= taken_rooms[0][0]:
            _, room_id = heapq.heappop(taken_rooms)
            idle_rooms.append(room_id)
        idle_rooms.sort(reverse=True)
        print(f"idle_rooms: {idle_rooms}")
        if idle_rooms:
            room_id = idle_rooms.pop()
            heapq.heappush(taken_rooms, [end, room_id])
            used_times[room_id] += 1
        else:
            previous_end, room_id = heapq.heappop(taken_rooms)
            if start < previous_end:
                heapq.heappush(taken_rooms, [end + (previous_end - start), room_id])
            else:
                heapq.heappush(taken_rooms, [end + previous_end, room_id])
            used_times[room_id] += 1

    return used_times


def organize_堆(self, n, meetings):
    """
    与上述方法的区别仅在于用堆而不是栈idle_rooms
    idel_rooms还可以用队列deque或者栈，但是都需要排序
    如果不排序，当一个meeting有不止一个会议室可选的时候，deque用popleft给出的是最早释放的会议室
    stack用pop给出的是最late释放的会议室
    如果没有充分理解题目，就会认为题目有个坑，没说清楚此种情况应该如何选，其实他想要编号最小的会议室
    其实这不是新情况，初始化的时候，就是每个会议有多个会议室可选。
    所以用了deque或者stack都需要在while循环结束后排序
    idle_rooms = deque(sorted(idle_rooms)), 且 队列没有sort()方法， 用sorted函数返回值是一个list，必须再重新转成deque，所以用deque最麻烦
    idle_rooms.sort(reverse=True)
    不如就用堆，总共两个堆，分别管理idle rooms和taken rooms
    """
    meetings.sort(key=lambda x: x[0])

    idle_rooms = list(range(1, n))
    heapq.heapify(idle_rooms)

    taken_rooms = [[meetings[0][1], 0]]
    heapq.heapify(taken_rooms)

    used_times = dict.fromkeys(range(n), 0)
    used_times[0] = 1

    for meeting in meetings[1:]:
        start, end = meeting
        while taken_rooms and start >= taken_rooms[0][0]:
            _, room_id = heapq.heappop(taken_rooms)
            heapq.heappush(idle_rooms, room_id)

        if idle_rooms:
            room_id = heapq.heappop(idle_rooms)
            heapq.heappush(taken_rooms, [end, room_id])
            used_times[room_id] += 1
        else:
            previous_end, room_id = heapq.heappop(taken_rooms)
            if start < previous_end:
                heapq.heappush(taken_rooms, [end + (previous_end - start), room_id])
            else:
                heapq.heappush(taken_rooms, [end + previous_end, room_id])
            used_times[room_id] += 1
    # next(iter(sorted(used_times.items(), key = lambda x: (-x[1], x[0]))))[0]
    return used_times


def most_booked_deque(n: int, meetings: List[List[int]]) -> int:
    meetings.sort(key=lambda x: x[0])
    idle_rooms = deque(range(n - 1, 0, -1))
    taken_rooms = [[meetings[0][1], 0]]
    used_times = dict.fromkeys(range(n), 0)
    used_times[0] = 1
    for meeting in meetings[1:]:
        start, end = meeting
        while taken_rooms and start >= taken_rooms[0][0]:
            _, room_id = heapq.heappop(taken_rooms)
            idle_rooms.append(room_id)
        idle_rooms.sort(reverse=True)
        print(f"idle_rooms: {idle_rooms}")
        if idle_rooms:
            room_id = idle_rooms.popleft()
            heapq.heappush(taken_rooms, [end, room_id])
            used_times[room_id] += 1
        else:
            previous_end, room_id = heapq.heappop(taken_rooms)
            if start < previous_end:
                heapq.heappush(taken_rooms, [end + (previous_end - start), room_id])
            else:
                heapq.heappush(taken_rooms, [end + previous_end, room_id])
            used_times[room_id] += 1

    return used_times


def most_booked2(n: int, meetings: List[List[int]]) -> int:
    meetings_count = defaultdict(int)
    rooms_end_time = [0] * n # room occupied till time
    queue = deque(sorted(meetings))

    while queue:
        t_start, t_end = queue.popleft()
        assigned = False
        for idx_room in range(n):
            # if room is available to use at time
            if rooms_end_time[idx_room]<= t_start:
                # update room occupied till time
                rooms_end_time[idx_room] = t_end
                meetings_count[idx_room] += 1
                assigned = True
                break

        if not assigned:
            # all meeting rooms are busy
            # get time of earliest free room
            # and add updated meeting to queue
            earliest_diff = min(rooms_end_time) - t_start
            queue.appendleft([t_start + earliest_diff, t_end + earliest_diff])

    meetings_count = dict(sorted(meetings_count.items(), key=lambda item: item[1], reverse=True))
    return next(iter(meetings_count))


class Solution2:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        heap = []
        free_room_heap = []
        for i in range(n):
            heapq.heappush(free_room_heap, (i, 0))

        heapq.heapify(meetings)
        while meetings:
            start, stop = heapq.heappop(meetings)

            while heap and heap[0][0] <= start:
                _, room, used = heapq.heappop(heap)
                heapq.heappush(free_room_heap, (room, used + 1))


                room, used = heapq.heappop(free_room_heap)
                ending_time = stop
            else:
                finish_time, room, used = heapq.heappop(heap)
                used += 1
                ending_time = finish_time + (stop - start)

            heapq.heappush(heap, (ending_time, room, used))

        while heap:
            _, room, used = heapq.heappop(heap)
            heapq.heappush(free_room_heap, (room, used + 1))

        ans = 0
        max_used = 0
        while free_room_heap:
            room, used = heapq.heappop(free_room_heap)
            if used > max_used:
                ans = room
                max_used = used
        return ans

    def mostBooked2(self, n: int, meetings: List[List[int]]) -> int:
        meetings_count = defaultdict(int)
        rooms = [0] * n  # room occupied till time
        queue = deque(sorted(meetings))

        while queue:
            meeting = queue.popleft()
            assigned = False
            for i in range(n):
                # if room is available to use at time
                if rooms[i] <= meeting[0]:
                    # update room occupied till time
                    rooms[i] = meeting[1]
                    meetings_count[i] += 1
                    assigned = True
                    break

            if not assigned:
                # all meeting rooms are busy
                # get time of earliest free room
                # and add updated meeting to queue
                earliest_diff = min(rooms) - meeting[0]
                queue.appendleft([meeting[0] + earliest_diff, meeting[1] + earliest_diff])

        meetings_count = dict(sorted(meetings_count.items(), key=lambda item: item[1], reverse=True))
        return next(iter(meetings_count))


class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """

        meetings.sort(key=lambda d: d[0])
        idle = list(range(n))
        min_time = []
        pending = []

        def start_meeting(idle, cnt, pending, min_time, now):
            room = heapq.heappop(idle)
            cnt[room] += 1
            meeting_info = heapq.heappop(pending)
            heapq.heappush(min_time, [now + meeting_info[1] - meeting_info[0], room])

        cnt = [0] * n
        for start_time, end_time in meetings:
            while min_time and min_time[0][0] <= start_time:
                now, num = heapq.heappop(min_time)
                heapq.heappush(idle, num)
                if pending:
                    start_meeting(idle, cnt, pending, min_time, now)

            heapq.heappush(pending, [start_time, end_time])
            if idle:
                start_meeting(idle, cnt, pending, min_time, start_time)

        while pending:
            if not idle:
                now = min_time[0][0]
                while min_time and min_time[0][0] == now:
                    _, num = heapq.heappop(min_time)
                    heapq.heappush(idle, num)

            start_meeting(idle, cnt, pending, min_time, now)

        res = 0
        for index in range(1, n):
            if cnt[index] > cnt[res]:
                res = index

        return res


if __name__ == "__main__":
    # n, meetings = 3, [[1,20],[2,10],[3,5],[4,9],[6,8]]
    # cnt = most_booked(n, meetings)
    # n, meetings = 2,[[0, 10], [1, 5], [2, 7], [3, 4]]
    # cnt2 = most_booked(n, meetings)
    n, meetings = 4, [[18,19],[3,12],[17,19],[2,13],[7,10]]
    cnt3 = most_booked(n, meetings)
    n, meetings = 4, [[48,49],[22,30],[13,31],[31,46],[37,46],[32,36],[25,36],[49,50],[24,34],[6,41]]
    cnt4 = most_booked(n, meetings)
    n, meetings = 5, [[12,18],[8,11],[19,20],[5,11]]
    cnt5 = most_booked(n, meetings)