# -*- coding: utf-8 -*-

"""
Tree Constructor Two
Have the function TreeConstructorTwo(strArr) take the array of strings stored in strArr,
which will contain pairs of integers in the following format: (i1, i2),
where i1 represents a child node in a tree and the second integer i2 signifies that it is the parent of i1.
For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the following tree:
        4
       /
      2
     / \
    1   7
which you can see forms a proper binary tree.
Your program should, in this case, return the string true because a valid binary tree can be formed.
If a proper binary tree cannot be formed with the integer pairs, then return the string false.
All of the integers within the tree will be unique,
which means there can only be one node in the tree with the given integer value.
"""


from collections import Counter
from typing import List
import re


def str2value_pair(tuple_str: str) -> tuple:
    return re.match(r"\(?(\d+)\,(\d+)\)?", tuple_str).groups()


def construct_tree(strArr: List[str]) -> bool:
    occurance_as_child = []
    occurance_as_parent = []

    for char in strArr:
        child_node, parent_node = str2value_pair(char)
        print(child_node, parent_node)
        # child_node, parent_node = eval(char)
        occurance_as_child.append(child_node)
        occurance_as_parent.append(parent_node)

    occurance_as_child_dict = Counter(occurance_as_child)
    occurance_as_parent_dict = Counter(occurance_as_parent)

    for parent_node in occurance_as_parent_dict:
        if occurance_as_parent_dict.get(parent_node) > 2:
            return False
    # each node is unique
    for child_node in occurance_as_child_dict:
        if occurance_as_child_dict.get(child_node) != 1:
            return False

    return True


if __name__ == "__main__":
    str_arr = ["(1,2)", "(2,432)", "(7,2)", "8,29"]
    for _ in str_arr:
        # m = re.match(r"\(?(\d+)\,(\d+)\)?", _)
        print(str2value_pair(_))



    print(construct_tree(["(1,2)", "(2,4)", "(7,2)"]))
    print(construct_tree(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))
    print(construct_tree(["(1,2)", "(3,2)", "(2,12)", "(5,2)"] ))

