# -*- coding: utf-8 -*-
"""
Created on Jul 05 18:49:20 2025

@author: Jerome Yutai Shen

"""
class Codec:
    def encode(self, strs: List[str]) -> str:
        # 每个字符串用 "长度#字符串" 编码
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # 找到分隔符的位置
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])     # 解析出长度
            i = j + 1
            res.append(s[i:i+length])  # 截取真正的字符串
            i += length
        return res