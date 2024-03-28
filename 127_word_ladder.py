# -*- coding: utf-8 -*-
"""
Created on Oct 21 14:54:54 2023

@author: Jerome Yutai Shen

"""
from collections import defaultdict, deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        Time Complexity: (O(M 2 ×N), where
        M is the length of each word and
        N is the total number of words in the input word list.
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(set)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].add(word)


        # Queue for BFS
        queue = deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = set()
        return 0


class Solution1:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        len_beginword = len(beginWord)
        all_combo_dict = self.get_all_combo_dict(wordList, len_beginword)

        return self.bfs_lc(beginWord, endWord, all_combo_dict)

    def get_all_combo_dict(self, wordList, len_beginword) -> dict:
        all_combo_dict = defaultdict(set)
        for word in wordList:
            for i in range(len_beginword):
                all_combo_dict[word[:i] + "*" + word[i + 1:]].add(word)
        return all_combo_dict

    def bfs_lc(self, beginWord, endWord, all_combo_dict) -> int:
        end_level = 0
        queue = deque([(beginWord, end_level + 1)])
        visited = {beginWord}
        current_words = []
        while queue:
            current_word, current_level = queue.popleft()
            for i in range(len(beginWord)):
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
                if not current_words or (current_word, current_level) != current_words[-1]:
                    current_words.append((current_word, current_level))
                #print(intermediate_word, all_combo_dict[intermediate_word], current_level, current_word, queue)
                for word in all_combo_dict[intermediate_word]:

                    if word == endWord:
                        current_words.append((word, current_level + 1))
                        print(current_words)
                        return current_level + 1

                    if word not in visited:
                        visited.add(word)
                        queue.append((word, current_level + 1))
        current_words = []
        return end_level


class BidirectionalBFS:
    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        queue_size = len(queue)
        for _ in range(queue_size):
            current_word = queue.popleft()
            for i in range(self.length):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

                # Next states are all the words which share the same intermediate state.
                for word in self.all_combo_dict[intermediate_word]:
                    # If the intermediate state/word has already been visited from the
                    # other parallel traversal this means we have found the answer.
                    if word in others_visited:
                        return visited[current_word] + others_visited[word]
                    if word not in visited:
                        # Save the level as the value of the dictionary, to save number of hops.
                        visited[word] = visited[current_word] + 1
                        queue.append(word)

        return None

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # Queues for birdirectional BFS
        queue_begin = deque([beginWord])  # BFS starting from beginWord
        queue_end = deque([endWord])  # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = { beginWord: 1 }
        visited_end = { endWord: 1 }
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # Progress forward one step from the shorter queue
            if len(queue_begin) <= len(queue_end):
                ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            else:
                ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    _ = Solution1()
    _.ladderLength(beginWord, endWord, wordList)