# -*- coding: utf-8 -*-
"""
Created on Apr 13 16:35:27 2023

@author: Jerome Yutai Shen

"""
from typing import List, Tuple
from enum import Enum, unique

@unique
class BankName(Enum):
    A = 1
    B = 2

class BankName(Enum):
    A = 1
    a = 1
    B = 2
    b = 2

class Bank:

    def __init__(self, this_bank: BankName, the_other_bank: BankName):
        self.this_bank, self.the_other_bank = this_bank, the_other_bank

    def get_min_initial(self, R: str, V: List[int]) -> int:
        balance = 0
        min_initial = 0
        for bank_name, value in zip(R, V):
            if bank_name == self.this_bank.name:
                delta = value
            else:
                assert bank_name == self.the_other_bank.name
                delta = -value
            balance += delta
            min_initial = min(min_initial, balance)

        return -min_initial

def solution(R: str, V: List[int]) -> Tuple[int, int]:
    assert len(R) == len(V)
    bank_a = Bank(BankName(1), BankName(2))
    bank_b = Bank(BankName(2), BankName(1))
    return (bank_a.get_min_initial(R, V), bank_b.get_min_initial(R, V))


def get_min_initial_b(R: str, V: List[int]) -> int:
    this_bank, the_other_bank = BankName(2), BankName(1)
    balance = 0
    min_initial = 0
    for bank_name, value in zip(R, V):
        if bank_name == this_bank.name:
            delta = value
        else:
            assert bank_name == the_other_bank.name
            delta = -value
        balance += delta
        min_initial = min(min_initial, balance)

    return -min_initial

def get_min_initial_a(R: str, V: List[int]) -> int:
    this_bank, the_other_bank = BankName(1), BankName(2)
    balance = 0
    min_initial = 0
    for bank_name, value in zip(R, V):
        if bank_name == this_bank.name:
            delta = value
        else:
            assert bank_name == the_other_bank.name
            delta = -value
        balance += delta
        min_initial = min(min_initial, balance)

    return -min_initial


if __name__ == "__main__":
    bank_a = Bank(BankName(1), BankName(2))
    bank_b = Bank(BankName(2), BankName(1))
    R, V = "BAABA", [2, 4, 1, 1, 2]
    print(solution(R, V))
    assert solution(R, V) == (get_min_initial_a(R, V), get_min_initial_b(R, V))
    R, V = "ABAB", [10, 5, 10, 15]
    print(solution(R, V))
    assert solution(R, V) == (get_min_initial_a(R, V), get_min_initial_b(R, V))
    R, V = "B", [100]
    print(solution(R, V))
    assert solution(R, V) == (get_min_initial_a(R, V), get_min_initial_b(R, V))
