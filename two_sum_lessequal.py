# -*- coding: utf-8 -*-
"""
PyCharm for binary_search.py

Created on Nov 19 11:02:23 2021

@author: Jerome Yutai Shen Y893565

"""

"""

DDBear

Publish at 2020-07-28

算法
算法一
暴力 **N^2N 
2
 **枚举

算法二 二分查找
二分知识
如果序列有序，则可以用一种更有效率的查找方法来查找序列中的记录，这就是折半查找法，又称为二分搜索。

折半查找的基本思想：减少一半的查找序列的长度，分而治之地进行关键字的查找。他的查找过程是：先确定待查找记录的所在的范围，然后逐渐缩小查找的范围，直至找到该记录为止（也可能查找失败）。

在最简单的形式中，二分查找对具有指定左索引和右索引的连续序列进行操作。这就是所谓的查找空间。二分查找维护查找空间的左、右和中间指示符，并比较查找目标或将查找条件应用于集合的中间值；如果条件不满足或值不相等，则清除目标不可能存在的那一半，并在剩下的一半上继续查找，直到成功为止。如果查以空的一半结束，则无法满足条件，并且无法找到目标。

算法思路
算法二在算法一的基础上进行改进

枚举一个数nums[i]nums[i],找有多少个j nums[i]+nums[j]<=targetnums[i]+nums[j]<=target

可以先对 numsnums排序 然后使用二分查找的方式快速查找

算法三 双指针
利用双指针 start，endstart，end求解

对于每个startstart，找到最大的endend，使得A[start]+B[end]A[start]+B[end]小于等于x

这样，因为数组是单调的，所以 A[start]+B[end+1]....A[start]+B[n-1]A[start]+B[end+1]....A[start]+B[n−1] 都大于xx

所以对于startstart,一共有end+1end+1对a+ba+b的和小于等于xx.

startstart移动到下一个位置，再去求新的endend

因为数组元素都是单调的，所以若A[start]+B[j]A[start]+B[j]大于xx，则A[start+1]+B[j]A[start+1]+B[j]一定也大于xx,所以，在startstart 移动到下一个位置时候，我们不需要重新从开始位置求一遍endend,而是在上一次求得end_lastend 
last基础上继续减少就可以了。

证明如下：

A[oldstart]+B[oldend] \leq xA[oldstart]+B[oldend]≤x

oldstart < newstartoldstart<newstart

所以A[oldstart]+B[oldend+1]>xA[oldstart]+B[oldend+1]>x

推出A[newstart]+B[oldend+1]>xA[newstart]+B[oldend+1]>x

所以newend \leq oldendnewend≤oldend

复杂度分析
空间复杂度

三个算法都不需要多开辟空间，因此空间复杂度为O(1)。
时间复杂度

算法一 暴力枚举**O(N^2)O(N 
2
 )**

算法二 枚举ii，用二分查找加速jj的数量 时间复杂度**O(NlogN)O(NlogN)**

算法三 双指针，start最多增加n次 end最多减少n次 所以时间复杂度**O(N)O(N)**
"""
class Solution:

    def two_pntrs(self, nums, target):
        # write your code here
        # 排序
        nums.sort()

        # 数组长度
        n = len(nums)

        # 答案
        ans = 0

        # 双指针上下界
        start = 0
        end = n - 1

        while start <= n - 1:

            # 找到最小的end nums[start]+nums[end]<=target
            while end >= 0:
                if nums[start] + nums[end] > target:
                    end -= 1
                else:
                    break

            # 只记录start<end的情况
            if end > start:
                ans += end - start
            else:
                break

            start += 1
        return ans