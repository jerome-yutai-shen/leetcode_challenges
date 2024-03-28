# -*- coding: utf-8 -*-
"""
Created on Feb 21 11:27:59 2024

@author: Jerome Yutai Shen

"""
This is just
a
simple
shared
plaintext
pad,
with no execution capabilities.

When
you
know
what
language
you
'd like to use for your interview,
simply
choose
it
from the dots

menu
on
the
tab, or add
a
new
language
tab
using
the
Languages
button
on
the
left.

You
can
also
change
the
default
language
your
pads
are
created
with
    in your
    account
    settings: https: // app.coderpad.io / settings

Enjoy
your
interview!



Given
a
positive
sorted
array
a = [3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21];

Define
a
function
f(a, x)
that
returns
x, the
next
smallest
number, or -1
for errors.
    I.e.f(a, 12) = 12;
    f(a, 13) = 12


def find_next_smallest(a: list, target: int) -> int:
    if not a:
        return -1
    import bisect
    idx = bisect.left(a, target)
    if 0 < idx < len(a):
        return a[idx - 1]
    else:
        return -1


def find_next_smallest2(a: list, target: int) -> int:
    if not a:
        return -1
    left, right = 0, len(a) - 1
    if target > a[-1]:
        return a[-1]
    if tagrt < a[0]:
        return -1
    while left + 1 < right:
        idx = (right - left) // 2
        if a[idx] < target:
            left = idx
        elif a[idx] > target:
            right = idx
        else:  # a[idx] == target
            return a[idx]
    return a[left]

// Test
Cases


def simple_test():
    assert find_next_smallest2([]) == -1

    a = [3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21]
    assert find_next_smallest2(a, 12) == 12
    assert find_next_smallest2(a, 13) == 12
    assert find_next_smallest2(a, 22) == 21
    assert find_next_smallest2(a, -2) == -1


Implement
a
moving
average
calculation
function.
// Function
to
compute
moving
average
// of
previous
K
elements
void
ComputeMovingAverage(int
arr[], int
N, int
K)

Input: { 1, 3, 5, 6, 8 }, K = 3
Output: 3.00
4.67
6.33


def compute_mov_avg(arr: int, n: int, k: int) -> list:
    """
    time complexity O(n)
    space O(n)
    """
    assert n == len(arr)
    if not arr:
        return [0.0]

    if n <= k:
        return [sum(arr) / n]

    res = []
    for end in range(k, n):
        start = 0 + (end - k)
        end = k + (end - k)
        res.append(sum(arr[start:end]) / k)

    return res


def compute_mov_avg2(arr: int, n: int, k: int) -> list:
    """
    time complexity O(n)
    space O(n)
    """
    assert n == len(arr)
    if not arr:
        return [0.0]

    if n <= k:
        return [sum(arr) / n]

    new_sum = sum(arr[:k])
    value_to_rmv = arr[0]
    res = [new_sum]

    for end in range(k, n):
        new_sum = new_sum + arr[k] - arr[0 + end - k]
        res.append(new_sum)
    return res

# streaming data  

def compute_mov_avg3(arr: list, k: int) -> list:
    """
    time complexity O(n)
    space O(n)
    """
    from collections import deque
    import numpy as np

    window = deque([], maxlen=k)
    res = []

    if not arr:
        return [None]

    for num in arr:
        window.append(num)
        if len(window) == k:
            res.append(np.mean(window))
    return res


if __name__ == "__main__":
    arr = [1, 3, 5, 6 ,8]
    k = 3
    compute_mov_avg3(arr, k)