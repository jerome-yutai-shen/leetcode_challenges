# -*- coding: utf-8 -*-
"""
Created on Jan 03 12:02:59 2024

@author: Jerome Yutai Shen

encoded str is like 'a3b4z55'
一个字母后面跟一串数字
面试官提示了edge case包括某个字母重复'a3b4z55a8'
"""
from collections import defaultdict
import re
PATTERN = r"[a-z][0-9]+"


class RLEDecoder:

    def __init__(self, raw_s: str):
        self.raw_s = raw_s
        self.char_cnt = defaultdict(int)
        self.str_decoder()
        assert(self.str_decoder2() == self.char_cnt)

    def __len__(self):
        _length = 0
        for k in self.char_cnt:
            _length += self.char_cnt.get(k)
        return _length

    def count(self, char):
        if char in self.char_cnt:
            return self.char_cnt.get(char)
        else:
            return 0

    def str_decoder(self):
        """正则表达式把时间复杂度提升了一个维度！
        用正则表达式 时间复杂度是O(TP) Let T,P be the lengths of the text and the pattern respectively."""
        _s = re.findall(PATTERN, self.raw_s)
        for c in _s:
            k, v = c[0], int(c[1:])
            self.char_cnt[k] += v

    def str_decoder2(self):
        """不用正则表达式"""
        k = ""
        v = ""
        char_cnt = defaultdict(int)

        for c in self.raw_s:
            if c.isalpha():
                if k and v:
                    char_cnt[k] += int(v)
                k = c
                v = ""
            else:
                assert c.isdigit()
                v += c

        assert (k and v)
        char_cnt[k] += int(v)

        return char_cnt


def str_decoder2(raw_s):
    k = ""
    v = ""
    char_cnt = defaultdict(int)

    for c in raw_s:
        if c.isalpha():
            if k and v:
                char_cnt[k] += int(v)
            k = c
            v = ""
        else:
            assert c.isdigit()
            v += c

    assert (k and v)
    char_cnt[k] += int(v)

    return char_cnt


def str_decoder(raw_s):
    """
    不用那么复杂吧
    """
    counts = defaultdict(int)
    idx = 0
    while idx < len(raw_s):
        char = raw_s[idx]
        idx += 1
        count = ""
        while idx < len(raw_s) and raw_s[idx].isdigit():
            count += raw_s[idx]
            idx += 1
        counts[char] += int(count)
    return dict(counts)


if __name__ == "__main__":
    '''
    print(str_decoder("a1b2z3a10"))
    print(str_decoder("a1b3z5a33"))
    '''

    s = "a1b2z3a10"
    rld = RLEDecoder(s)
    print(len(rld), rld.count("a"), rld.count("h"))
    print(rld.str_decoder2(), rld.char_cnt)

    s = "a1b3z5a33"
    rld1 = RLEDecoder(s)
    print(len(rld1), rld1.count("a"), rld1.count("h"))
    print(rld1.str_decoder2(), rld1.char_cnt)