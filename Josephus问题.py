# -*- coding: utf-8 -*-
"""
Created on Jan 09 10:10:41 2024

@author: Jerome Yutai Shen

"""


# Python code for Josephus Problem
def Josh(person, k, index):
    # Base case , when only one person is left
    if len(person) == 1:
        print(person[0])
        return

    # find the index of first person which will die
    index = ((index + k) % len(person))

    # remove the first person which is going to be killed
    person.pop(index)

    # recursive call for n-1 persons
    Josh(person, k, index)


def Josephus(n, k):
    # initialize two variables i and ans
    i = 1
    ans = 1
    while (i <= n):
        # update the value of ans
        ans = (ans + k) % i
        i += 1
        print(f"ans{ans}i{i}")

    # returning the required answer
    return ans + 1


# driver code


# This code is contributed by
# Gaurav Kandel

class node(object):
    def __init__(self, id, next = None):
        self.id = id
        self.next = next

class Solution:
    """
    @param n: an integer
    @param k: an integer
    @return: the last person's number
    """
    def josephProblem(self, n, k):
        # Write your code here
        head = node(0)
        cur = head
        for i in range(1, n):
            nx = node(i)
            cur.next = nx
            cur = cur.next
        cur.next = head
        sum = 0
        while True:
            for i in range(k - 1):
                cur = cur.next
            cur.next = cur.next.next
            sum += 1
            if sum == n - 1:
                break
        return cur.id


def j_f1(n, k):
    s = 0
    for idx in range(2, n + 1):
        s = (s + k) % idx
    return s + 1


def j_f0(n, k):
    s = 0
    for idx in range(2, n + 1):
        s = (s + k) % idx
    return s


if __name__ == "__main__":
    # let
    n = 14
    k = 2

    result = Josephus(n, k)
    print("Josephus", result)

    # This code is contributed by sarveshc111.

    # Driver Program to test above function
    n = 14  # specific n and k  values for original josephus problem
    k = 2
    k -= 1  # (k-1)th person will be killed

    index = 0

    # fill the person vector
    person = []
    for i in range(1, n + 1):
        person.append(i)

    print("Josh", Josh(person, k, index))


    sl = Solution()
    print("九章", sl.josephProblem(n, k))

    n, k = 14, 2
    print(f"j_f: {j_f(n ,k)}")