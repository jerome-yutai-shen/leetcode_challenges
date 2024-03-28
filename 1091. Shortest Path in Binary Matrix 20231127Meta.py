# -*- coding: utf-8 -*-
"""
Created on Nov 27 11:06:16 2023

@author: Jerome Yutai Shen
2023年11月27日面试题
接近于1926
"""
from typing import List
from collections import deque


class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

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
        queue = deque([(0, 0)])
        visited = { (0, 0) }
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

# d当时我的代码


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:

    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    directions = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # 我写的是四个方向

    # Check that the first and last cells are open.
    if grid[0][0] != 0 or grid[max_row][max_col] != 0:
        return -1

    # Set up the BFS.
    queue = deque([(0, 0)])
    visited = { (0, 0) }
    current_distance = 1
    path = []

    # Do the BFS.
    while queue:
        # Process all nodes at current_distance from the top-left cell.
        nodes_of_current_distance = len(queue)
        for _ in range(nodes_of_current_distance):
            row, col = queue.popleft()
            path.append((row, col))
            if (row, col) == (max_row, max_col):
                return current_distance

            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                neighbour = (new_row, new_col)

                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue

                if neighbour in visited:
                    continue
                visited.add(neighbour)
                queue.append(neighbour)
        # We'll now be processing all nodes at current_distance + 1
        current_distance += 1

    # print(path)
    # There was no path.
    return -1


DIRECTIONS = ( (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def shortestPathBinaryMatrix3(grid: List[List[int]]) -> List:
    """
    要求打印路径
    """
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    directions = DIRECTIONS
        # 我写的是四个方向 directions((0, 1), (1, 0), (0, -1), (-1, 0))

    entrance = (0, 0)
    exit = (max_row, max_col)

    path = []

    # Check that the first and last cells are open.
    if grid[entrance[0]][entrance[-1]] != 0 or grid[exit[0]][exit[-1]] != 0:
        return path

    # Set up the BFS.

    queue = deque([entrance])
    visited = {entrance}
    current_distance = 1


    # Do the BFS.
    while queue:
        # Process all nodes at current_distance from the top-left cell.
        nodes_of_current_distance = len(queue)
        for _ in range(nodes_of_current_distance):
            row, col = queue.popleft()
            path.append((row, col))
            if (row, col) == exit:
                return path

            for dy, dx in directions:
                new_row = row + dy
                new_col = col + dx
                neighbour = (new_row, new_col)

                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue

                if neighbour in visited:
                    continue
                visited.add(neighbour)
                queue.append(neighbour)
        # We'll now be processing all nodes at current_distance + 1
        current_distance += 1


    # There was no path.
    return []


if __name__ == "__main__":
    grid = [[0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1],
            [0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0]]
    path = shortestPathBinaryMatrix3(grid)

    grid2 = [ [0] * len(grid[0]) for _ in range(len(grid))]
    for _ in path:
        grid2[_[0]][_[1]] = "+"