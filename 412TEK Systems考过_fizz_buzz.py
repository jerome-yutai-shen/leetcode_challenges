# -*- coding: utf-8 -*-
"""
Created on Apr 28 12:27:46 2023

@author: Jerome Yutai Shen

TEK Systems考过

"""


def fizzBuzz(n):
    # Write your code here

    ans = []

    divisors = (3, 5)
    fizz_buzz_dict = dict(zip(divisors, ("Fizz", "Buzz")))

    for num in range(1, n + 1):

        num_ans_str = []

        for key in fizz_buzz_dict:
            if num % key == 0:
                num_ans_str.append(fizz_buzz_dict.get(key))

        if not num_ans_str:
            num_ans_str.append(str(num))

        ans.append("".join(num_ans_str))
        print("".join(num_ans_str))
    return ans


if __name__ == "__main__":
    for n in [15, 18]:
        fizzBuzz(n)
