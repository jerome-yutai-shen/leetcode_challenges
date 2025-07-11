# -*- coding: utf-8 -*-
"""
Created on Sep 07 19:48:24 2023

@author: Jerome Yutai Shen

"""
class Solution:
    def wordPatternMatch(self, pattern, str):
        return self.dfs(pattern, str, {})

    def dfs(self, pattern, str, dict):
        if len(pattern) == 0 and len(str) > 0:
            return False
        if len(pattern) == len(str) == 0:
            return True
        for end in range(1, len(str)-len(pattern)+2): # +2 because it is the "end of an end"
            if pattern[0] not in dict and str[:end] not in dict.values():
                dict[pattern[0]] = str[:end]
                if self.dfs(pattern[1:], str[end:], dict):
                    return True
                del dict[pattern[0]]
            elif pattern[0] in dict and dict[pattern[0]] == str[:end]:
                if self.dfs(pattern[1:], str[end:], dict):
                    return True
        return False


class Solution2:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        p_len, s_len = len(pattern), len(s)

        char_to_word = { }
        word_to_char = { }

        def dfs(i: int, j: int) -> bool:
            if i == p_len and j == s_len:
                # reached the end to both pattern and s
                # we got a match
                return True

            if i == p_len or j == s_len:
                # reached the end of one but not the other
                # we do not have a match
                return False

            # for each possible "word" in s
            for k in range(j, s_len):
                # our current pattern
                c = pattern[i]

                # possible "word" in s
                word = s[j:k + 1]

                if c not in char_to_word and word not in word_to_char:
                    # newly seen pattern character and "word"
                    char_to_word[c] = word
                    word_to_char[word] = c

                    if dfs(i + 1, k + 1):
                        return True

                    # didn't find a match, backtrack
                    del char_to_word[c]
                    del word_to_char[word]

                elif c not in char_to_word or word not in word_to_char:
                    # either c is already used, or word is already matched
                    # we ignore this combination and keep looking
                    continue

                elif char_to_word[c] == word and word_to_char[word] == c:
                    # this combination is consistent with what we've matched
                    # so far, so we can keep going without backtracking
                    if dfs(i + 1, k + 1):
                        return True

            # exhausted our possibilities, no match found
            return False

        return dfs(0, 0)


"""
dfs(pi, si):
├── base case: pattern和s都走完，匹配成功
├── 如果当前 ch 已经映射：
│   ├── 看 s[si:] 是否能匹配 word
│   └── 不能匹配直接剪枝
└── 如果 ch 还未映射：
    └── for end in si+1 to len(s)+1
        ├── candidate = s[si:end]
        ├── 如果 candidate 已经被映射，跳过
        ├── 建立映射 ch → candidate
        ├── dfs(pi+1, end)
        └── 回溯
"""

class Solution_dict_set:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.dfs(0, 0, pattern, s, {}, set())

    def dfs(self, pi: int, si: int, pattern: str, s: str,
            mapping: dict, used: set) -> bool:
        # base case: pattern和s都走完，匹配成功
        if pi == len(pattern) and si == len(s):
            return True
        # 如果一个走完另一个没走完 则返回False
        if pi == len(pattern) or si == len(s):
            return False
        # 都没走完就继续

        # ├── 如果当前 ch 已经映射：
        # │   ├── 看 s[si:] 是否能匹配 word
        # │   └── 不能匹配直接剪枝

        ch = pattern[pi]
        # 递归拆解， 分两种情况
        # # 已存在映射，直接验证后递归

        if ch in mapping:
            word = mapping[ch]
            if not s.startswith(word, si):
                return False
            return self.dfs(pi + 1, si + len(word), pattern, s, mapping, used)

        # # 不存在映射，枚举所有可能的子串尝试建立映射：
        for end in range(si + 1, len(s) + 1):
            candidate = s[si:end]
            if candidate in used:
                continue

            # 建立双向映射
            mapping[ch] = candidate
            used.add(candidate)

            if self.dfs(pi + 1, end, pattern, s, mapping, used):
                return True

            # 回溯
            del mapping[ch]
            used.remove(candidate)

        return False


class Solution_Two_dict:

    def wordPatternMatch(self, pattern: str, s: str):
        return self.dfs(0, 0, pattern, s, { }, { })

    def dfs(self, pi: int, si: int, pattern: str, s: str,
            pattern_word: dict, word_pattern: set) -> bool:
        # 递归出口
        if pi == len(pattern) and si == len(s):
            return True
        if pi == len(pattern) or si == len(s):
            return False

        # 递归拆解， 分两种情况
        # # 已存在映射，直接验证后递归
        ch = pattern[pi]

        if ch in pattern_word:
            word = pattern_word[ch]
            if not s.startswith(word, si):
                return False
            return self.dfs(pi + 1, si + len(word), pattern, s, pattern_word, word_pattern)

        # # 不存在映射，枚举所有可能的子串尝试建立映射：
        for end in range(si + 1, len(s) + 1):
            candidate = s[si:end]
            if candidate in word_pattern:
                continue

            # 建立双向映射
            pattern_word[ch] = candidate
            word_pattern[candidate] = ch

            if self.dfs(pi + 1, end, pattern, s, pattern_word, word_pattern):
                return True

            # 回溯
            del pattern_word[ch]
            del word_pattern[candidate]

        return False


if __name__ == "__main__":
    pattern = "abab"
    s = "redblueredblue"
    solution = Solution()