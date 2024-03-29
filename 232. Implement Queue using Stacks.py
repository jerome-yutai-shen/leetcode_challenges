# -*- coding: utf-8 -*-
"""
Created on Jan 08 16:57:03 2024

@author: Jerome Yutai Shen

"""


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        self.stack1.append(element)

    """
    @return: An integer
    """

    def pop(self):
        if len(self.stack2) == 0:
            self.move()
        return self.stack2.pop()

    """
    @return: An integer
    """

    def peek(self):
        if len(self.stack2) == 0:
            self.move()
        return self.stack2[-1]

    # 从1号栈转移到2号栈
    def move(self):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

    def empty(self):
        return not self.stack1 and not self.stack2