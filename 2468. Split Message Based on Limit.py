# -*- coding: utf-8 -*-
"""
Created on Feb 13 01:29:28 2024

@author: Jerome Yutai Shen

"""


def splitMessage(self, message: str, limit: int) -> list:
    '''
    message: str, "this is really a very awesome message"
    limit: int, 9
    O(n*m), O(1)
    '''
    num_parts = numerator_len = 1
    res = []

    while num_parts * (len(str(num_parts)) + 3) + numerator_len + len(message) > num_parts * limit:
        if 3 + len(str(num_parts)) * 2 >= limit: return res
        num_parts += 1
        numerator_len += len(str(num_parts))

    for i in range(1, num_parts + 1):
        j = limit - (len(str(i)) + len(str(num_parts)) + 3)
        part, message = message[:j], message[j:]
        res.append(part + "<" + str(i) + "/" + str(num_parts) + ">")

    return res