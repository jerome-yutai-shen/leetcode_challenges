# -*- coding: utf-8 -*-
"""
Created on Feb 15 13:49:10 2024

@author: Jerome Yutai Shen

"""
def remove_d_a(msg):
    res = []
    for c in msg:
        if not res:
            res.append(c)
        elif res[-1] == c:
            res.pop()
        else:
            res.append(c)
    return "".join(res)


if __name__ == "__main__":
    print(remove_d_a("aaac"))
    print(remove_d_a("aaca"))