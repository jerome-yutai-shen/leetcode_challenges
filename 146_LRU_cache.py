# -*- coding: utf-8 -*-
"""
Created on Apr 18 09:19:42 2023

@author: Jerome Yutai Shen

"""
from collections import OrderedDict, deque


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key: int):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1

        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


class LRUCache2:
    # 尝试用双端队列 发现是错的 O(N) not O(1)

    def __init__(self, capacity: int):
        """
        :type capacity: int
        """
        self.map = dict()
        self.keys = deque([])
        self.capacity = capacity

    def get(self, key: int):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1

        self.keys.append(key)
        return self[key]

    def put(self, key: int, value: int):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.map:
            self.keys.append(key)
        self[key] = value
        if len(self) > self.capacity:
            _k = self.keys.popleft()
            self.map.pop(_k)


class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache3():

    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)

        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)


if __name__ == "__main__":
    lru_cache = LRUCache(2)
    for k, v in [(1, 1), (2, 2), (3, 3), (4, 4)]:
        lru_cache.put(k, v)
        print(lru_cache)