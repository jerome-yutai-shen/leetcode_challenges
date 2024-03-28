# -*- coding: utf-8 -*-
"""
Created on Oct 02 11:07:36 2023

@author: Jerome Yutai Shen

"""
from collections.abc import Sequence
from dataclasses import dataclass
from math import sqrt
from typing import Tuple, List, Set
from collections import defaultdict


@dataclass(frozen=True, eq=True)
class Flower:
    name: str
    x: float
    y: float
    bloom_radius: float

    def distance(self, other: "Flower") -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def check_relationship(flowers: Sequence[Flower]):
    """
    cyclic directed graph, A->B !=> B->A
    """
    distances_bloom = { }
    for flower in flowers:
        for flower1 in flowers:
            if flower.name == flower1.name:
                continue
            curr_pair = tuple([flower.name, flower1.name])
            distance = flower.distance(flower1)
            if_bloom = flower.bloom_radius >= distance
            distances_bloom[curr_pair] = (distance, if_bloom)

    return distances_bloom


def check_flower(flowers: Sequence[Flower]):
    distances_bloom = check_relationship(flowers)
    children_1storder = defaultdict(set)

    for flower_pair in distances_bloom:
        if distances_bloom.get(flower_pair)[1]:
            flower = flower_pair[0]
            children_1storder[flower_pair[0]].add(flower_pair[1])
    return children_1storder


def dfs(children: dict, key: str, visited: set) -> Set:
    """
    DFS, recurrsion
    """
    nodes = children.get(key)
    if not nodes:
        return set()

    if key in visited:
        return set()
    visited.add(key)

    for node in nodes:
        children2 = dfs(children, node, visited)
        nodes = nodes.union(children2)

    if key in nodes:
        nodes = nodes - {key}
    return nodes


def most_flowers(flowers: Sequence[Flower]) -> Tuple[str, int]:
    """Finds the largest superbloom.

    Returns the name of the starting flower, and the number of flowers
    that bloom.
    """

    # 🌼 Your code goes here! 🌼
    children_1st_generation = check_flower(flowers)
    max_total_flowers = 0
    biggest_flower = ""
    for flower in children_1st_generation:
        _all_children = dfs(children_1st_generation,
                                   flower,
                                   set())
        _total_flowers = len(_all_children) + 1
        if _total_flowers > max_total_flowers:
            biggest_flower = flower
            max_total_flowers = _total_flowers
        # print(flower, _all_children)
    return biggest_flower, max_total_flowers,


if __name__ == "__main__":
    flowers = [
        Flower("A", 7, 13, 3),
        Flower("B", 6.5, 17, 5),
        Flower("C", 12, 10, 4.5),
        Flower("D", 14.5, 7, 3.5),
        Flower("E", 17, 9, 2),
        Flower("F", 7, 11, 2.5),
        Flower("G", 8.5, 11.5, 3),
    ]
    children_1st_generation = check_flower(flowers)
    _all_children = dfs(children_1st_generation, 'A', set())
    assert most_flowers(flowers) == ("C", 6)

