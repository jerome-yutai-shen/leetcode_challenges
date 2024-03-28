# -*- coding: utf-8 -*-
"""
Created on Nov 11 14:43:40 2023

@author: Jerome Yutai Shen

"""
class Solution2:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s: str) -> int:
        bracket_stack = []
        result = 0
        number = 0
        next_sign = 1
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c == '+':
                result += next_sign * number
                number = 0
                next_sign = 1
            elif c == '-':
                result += next_sign * number
                number = 0
                next_sign = -1
            elif c == '(':
                bracket_stack.append(result)
                bracket_stack.append(next_sign)
                next_sign = 1
                result = 0
            elif c == ')':
                result += next_sign * number
                number = 0
                print(bracket_stack)
                _ = bracket_stack.pop()
                result *= _
                _ = bracket_stack.pop()
                result += _

        result += next_sign * number
        return result


class Solution:
    def calculate(self, s: str) -> int:
        """
        初始operand, result = 0, sign = 1, 开始遍历字符串:

        碰到数字则追加到operand尾端
        碰到加号说明上一个数字已经完全被计算至operand, 这时应该把operand * sign加到result中, 然后把sign置为1 (因为当前碰到了加号)，operand清零
        碰到减号, 同上, 不同的在于最后要把sign置为-1，operand清零
        碰到左括号, 说明这时要优先出右边的表达式, 需要将result和sign压入栈中(注意, 此时的sign表示的是这个括号内的表达式应该被operand加上还是减去), 然后初始化result和sign, 准备计算括号内的表达式
        碰到右括号, 说明一个括号内的表达式被计算完了, 此时需要从栈中取出该括号之前的sign和result, 与当前的result相加运算 (注意, 是原来的result + sign * 当前result)
        注意, 一个合法的表达式, 左括号之前一定不会是数字, 右括号之前一定是一个数字. 所以碰到右括号不要忘了先把operand * sign加到当前result里.

        以及, 循环结束后number可能还有数字, 需要加到result里. (比如"1+2"这样的表达式, 2并不会在循环内被加到结果中)
        """

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':
                print(stack)
                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand


if __name__ == "__main__":
    _ = Solution()
    s = "1+2-3"
    _.calculate(s)
    s = "7 - (8 + 9)"
    _.calculate(s)
    s = "(1+(4+5+2)-3)+(6+8)"
    _.calculate(s)

