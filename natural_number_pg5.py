# -*- coding: utf-8 -*-
"""
Created on May 29 17:38:46 2023

@author: Jerome Yutai Shen
郇中丹2009简明数学分析
"""


class NaturalNumber:

    def __init__(self, n: int):
        self.set = list(range(n))
        self.value = n
        self.__name_itself()

    def plus_one(self):
        self.set.append(self.value)
        self.value += 1
        self.__name_itself()

    def __name_itself(self):
        self.name = f"natural number: {str(self.value)}"


if __name__ == "__main__":
    n_n = NaturalNumber(3)
    print(n_n.set, n_n.value, n_n.name)
    n_n.plus_one()
    print(n_n.set, n_n.value, n_n.name)

    n_n = NaturalNumber(18)
    print(n_n.set, n_n.value, n_n.name)
    n_n.plus_one()
    print(n_n.set, n_n.value, n_n.name)