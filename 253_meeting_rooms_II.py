# -*- coding: utf-8 -*-
"""
Created on Nov 12 15:25:23 2023

@author: Jerome Yutai Shen

"""
from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        first_end = intervals[0][1]
        heapq.heappush(free_rooms, first_end)

        # For all the remaining meeting rooms
        for interval in intervals[1:]:
            current_start, current_end = interval
            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= current_start:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, current_end)

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    _ = Solution()
    _.minMeetingRooms(intervals)