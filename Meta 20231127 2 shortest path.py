# -*- coding: utf-8 -*-
"""
Created on Nov 28 15:27:18 2023

@author: Jerome Yutai Shen
leetcode 1091 的变体
要求给出最短路径本身而不是最短路径的长度

https://www.techiedelight.com/find-shortest-path-source-destination-matrix-satisfies-given-constraints/

现在才知道当时错了，错在给出的是所有搜索路径，不是真的最短路径

"""
from collections import deque
from typing import Tuple, List, Optional, FrozenSet


# A queue node used in BFS
class Node:
    # (x, y) represents coordinates of a cell in the matrix
    # maintain a parent node for the printing path
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def __repr__(self):
        return str((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Below lists detail all four possible movements from a cell
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]


# The function returns false if (x, y) is not a valid position
def isValid(x, y, N):
    return (0 <= x < N) and (0 <= y < N)


# Utility function to find path from source to destination
def getPath(node, path=[]):
    if node:
        getPath(node.parent, path)
        path.append(node)


# Find the shortest route in a matrix from source cell (x, y) to
# destination cell (N-1, N-1)
def findPath(matrix, x=0, y=0):
    # base case
    if not matrix or not len(matrix):
        return

    # `N × N` matrix
    N = len(matrix)

    # create a queue and enqueue the first node
    q = deque()
    src = Node(x, y)
    q.append(src)

    # set to check if the matrix cell is visited before or not
    visited = set()

    key = (src.x, src.y)
    visited.add(key)

    # loop till queue is empty
    while q:

        # dequeue front node and process it

        curr = q.popleft()
        i = curr.x
        j = curr.y

        # return if the destination is found
        if i == N - 1 and j == N - 1:
            path = []
            getPath(curr, path)
            return path

        # value of the current cell
        n = matrix[i][j]

        # check all four possible movements from the current cell
        # and recur for each valid movement
        for k in range(len(row)):
            # get next position coordinates using the value of the current cell
            x = i + row[k] * n
            y = j + col[k] * n

            # check if it is possible to go to the next position
            # from the current position
            if isValid(x, y, N):
                # construct the next cell node
                next = Node(x, y, curr)
                key = (next.x, next.y)

                # if it isn't visited yet
                if key not in visited:
                    # enqueue it and mark it as visited
                    q.append(next)
                    visited.add(key)

    # return None if the path is not possible
    return


DIRECTIONS = frozenset({(_, __) for _ in range(-1, 2) for __ in range(-1, 2)} - {(0, 0)})
DIRECTIONS2 = frozenset({(0, -1), (-1, 0), (1, 0), (0, 1)}) # 我写的是四个方向 directions((0, 1), (1, 0), (0, -1), (-1, 0)) 这一点竟然没跟面试官确认
# 实际上应该是八个方向

class GridNode:
    def __init__(self, position: Tuple[int, int], prev: Optional = None):
        self.position = position
        self.prev = prev


def shortestPathBinaryMatrix3(grid: Optional[List[List[int]]], directions: FrozenSet[Tuple[int, int]] = DIRECTIONS) -> Tuple:
    """
    要求打印路径
    """
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1

    entrance = (0, 0)
    exit = (max_row, max_col)

    # Check that the first and last cells are open.
    if grid[entrance[0]][entrance[-1]] != 0 or grid[exit[0]][exit[-1]] != 0:
        print(grid[entrance[0]][entrance[-1]], grid[exit[0]][exit[-1]])
        return [], -1

    queue = deque([GridNode(entrance)])
    visited = set()
    current_distance = 1

    while queue:
        nodes_of_current_distance = len(queue)
        for _ in range(nodes_of_current_distance):
            node = queue.popleft()
            row, col = node.position
            if (row, col) in visited:
                continue
            visited.add((row, col))

            if (row, col) == exit:
                path = get_path(node)
                assert len(path) == current_distance
                return path, current_distance

            for dy, dx in directions:
                new_row = row + dy
                new_col = col + dx
                neighbour = (new_row, new_col)

                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                new_node = GridNode(neighbour, node)
                queue.append(new_node)

        current_distance += 1

    return [], -1


def get_path(node: GridNode) -> Tuple[Tuple[int, int]]:
    path = deque([node.position])
    while node.prev:
        node = node.prev
        path.appendleft(node.position)
    return tuple(path)


class Leetcode1091:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """BFS 先标记访问后入队列"""
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)

        # Check that the first and last cells are open.
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        # Set up the BFS.
        visited = { (0, 0) }
        queue = deque([(0, 0)])

        current_distance = 1

        # Do the BFS.
        while queue:
            # Process all nodes at current_distance from the top-left cell.
            nodes_of_current_distance = len(queue)
            for _ in range(nodes_of_current_distance):
                row, col = queue.popleft()
                if (row, col) == (max_row, max_col):
                    return current_distance
                for neighbour in get_neighbours(row, col):
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    queue.append(neighbour)
            # We'll now be processing all nodes at current_distance + 1
            current_distance += 1

        # There was no path.
        return -1


DIRECTIONS = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1),


class Solution2:


    def get_neighbours(self, row: int, col: int, grid: List[List[int]], directions: Tuple[Tuple[int, int]] = DIRECTIONS) -> List[
        Tuple[int, int]]:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        result = []
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row <= max_row and 0 <= new_col <= max_col:
                if grid[new_row][new_col] == 0:
                    result.append((new_row, new_col))
        return result

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        visited = { (0, 0) }
        queue = deque([(0, 0)])
        current_distance = 1

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if (row, col) == (max_row, max_col):
                    return current_distance
                for neighbour in self.get_neighbours(row, col, grid):
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            current_distance += 1

        return -1


class Solution3:


    def get_neighbours(self, row: int, col: int, grid: List[List[int]], directions: Tuple[Tuple[int, int]] = DIRECTIONS) -> List[
        Tuple[int, int]]:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        result = []
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row <= max_row and 0 <= new_col <= max_col:
                if grid[new_row][new_col] == 0:
                    result.append((new_row, new_col))
        return result

    def get_path(self, prev_pos: dict, pos: tuple[int, int]) -> list:
        res = []
        res.append(pos)

        while pos is not None:
            pos = prev_pos[pos]
            res.append(pos)

        return res[::-1]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        visited = { (0, 0) }
        queue = deque([(0, 0)])
        current_distance = 1
        prev_pos = {(0, 0): None}
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if (row, col) == (max_row, max_col):
                    target_path = self.get_path(prev_pos, (row, col))
                    assert len(target_path) == current_distance + 1
                    return current_distance + 1

                for neighbour in self.get_neighbours(row, col, grid):
                    prev_pos[neighbour] = (row, col)

                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            current_distance += 1

        return -1


if __name__ == '__main__':

    matrix = [
        [4, 4, 6, 5, 5, 1, 1, 1, 7, 4],
        [3, 6, 2, 4, 6, 5, 7, 2, 6, 6],
        [1, 3, 6, 1, 1, 1, 7, 1, 4, 5],
        [7, 5, 6, 3, 1, 3, 3, 1, 1, 7],
        [3, 4, 6, 4, 7, 2, 6, 5, 4, 4],
        [3, 2, 5, 1, 2, 5, 1, 2, 3, 4],
        [4, 2, 2, 2, 5, 2, 3, 7, 7, 3],
        [7, 2, 4, 3, 5, 2, 2, 3, 6, 3],
        [5, 1, 4, 2, 6, 4, 6, 7, 3, 7],
        [1, 4, 1, 7, 5, 3, 6, 5, 3, 4]
    ]

    # Find a route in the matrix from source cell (0, 0) to
    # destination cell (N-1, N-1)
    path = findPath(matrix)

    if path:
        print('The shortest path is', path)
    else:
        print('Destination is not found')

    grid = [[0, 0, 1],
              [0, 0, 1],
              [0, 0, 0]]
    path, current_distance = shortestPathBinaryMatrix3(grid)
    path2, current_distance2 = shortestPathBinaryMatrix3(grid, DIRECTIONS2)

    grid = [[0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0]]
    path3, current_distance3 = shortestPathBinaryMatrix3(grid)
    path4, current_distance4 = shortestPathBinaryMatrix3(grid, DIRECTIONS2)

    grid = [[0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0]]