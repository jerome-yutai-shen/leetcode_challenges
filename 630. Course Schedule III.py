# -*- coding: utf-8 -*-
"""
Created on Jul 04 17:54:03 2025

@author: Jerome Yutai Shen

"""
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])  # 按结束时间排序
        max_heap = []
        total_time = 0

        for duration, lastDay in courses:
            total_time += duration
            heapq.heappush(max_heap, -duration)  # Python最小堆变最大堆
            if total_time > lastDay:
                # 超时了，撤销一门最耗时的课
                longest = -heapq.heappop(max_heap)
                total_time -= longest

        return len(max_heap)

    def scheduleCourse2(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])  # 先按结束时间排序
        max_heap = []
        time = 0

        for duration, end in courses:
            time += duration
            heapq.heappush(max_heap, -duration)  # 最大堆：用负数
            if time > end:
                time += heapq.heappop(max_heap)  # 删除最长的一门课

        return len(max_heap)
"""
一般贪心题我们会问：

“到底贪什么？”

这题的贪心点是：
	•	优先选择 early deadline（lastDay 小）的课
	•	一旦时间超了，就把“耗时最长的课”换掉

这个策略其实是近似背包 + 优化调度，但不直接。很多人会问：
	•	“为什么不能选 duration 最小的？”
	•	“为什么不是 lastDay 最小的？”

✅ 实际上它是一个贪心 + 替换策略

“能加就加；加不了就替换当前最长耗时的一门。”

这种贪心策略，不是直觉能想到的。

我们“贪”的是：在总时间不超的前提下，尽可能多选课程，而不是选最短的、最早的、最晚的。

⸻

🧠 为什么贪心目标是“最多课程数量”？

题目明确说：

You want to take as many courses as possible.

	•	每门课程的持续时间不同
	•	每门课程必须在 lastDay 前结束
	•	所以你不能乱选，也不能简单取前 k 个

⸻

✅ 实际策略是：在合法的时间窗口内塞最多的课

而要实现这个目标，就要：

1️⃣ 优先考虑“截止时间早”的课（按 lastDay 排序）
	•	否则你会错过早截止的课程

2️⃣ 一旦总时长超了，就“踢掉最长的一门课”
	•	因为踢掉一个耗时长的，可能腾出时间容纳更多课
	•	这就是为什么用最大堆存当前选过的课，动态维护一个“最耗时的课”，必要时替换掉
⸻

3️⃣ 最大堆不常见 + Python 不支持

Python 默认是 最小堆（heapq），所以我们得手动取负值：
"""
""