# -*- coding: utf-8 -*-
"""
Created on Apr 18 10:10:37 2023

@author: Jerome Yutai Shen

"""
from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []

    for token in tokens:

        if token not in "+-/*":
            stack.append(int(token))
            continue

        number_2 = stack.pop()
        number_1 = stack.pop()

        result = 0
        if token == "+":
            result = number_1 + number_2
        elif token == "-":
            result = number_1 - number_2
        elif token == "*":
            result = number_1 * number_2
        else:
            result = int(number_1 / number_2)

        stack.append(result)

    return stack.pop()


def evalRPN2(tokens: List[str]) -> int:

    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
    }

    current_position = 0

    while len(tokens) > 1:

        # Move the current position pointer to the next operator.
        while tokens[current_position] not in "+-*/":
            current_position += 1

        # Extract the operator and numbers from the list.
        operator = tokens[current_position]
        number_1 = int(tokens[current_position - 2])
        number_2 = int(tokens[current_position - 1])

        # Calculate the result to overwrite the operator with.
        operation = operations[operator]
        tokens[current_position] = operation(number_1, number_2)

        # Remove the numbers and move the pointer to the position
        # after the new number we just added.
        tokens.pop(current_position - 2)
        tokens.pop(current_position - 2)
        current_position -= 1

    return int(tokens[0])



if __name__ == "__main__":
    print(evalRPN2(["18"]))