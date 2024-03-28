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


if __name__ == "__main__":
    pattern = "abab"
    s = "redblueredblue"
    solution = Solution()