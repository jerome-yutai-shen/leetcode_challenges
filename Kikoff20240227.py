# -*- coding: utf-8 -*-
"""
Created on Feb 27 11:56:45 2024

@author: Jerome Yutai Shen

"""

"""
input "( + 1  2 )"  output 3.0
input "(  - ( + 15  2 ) ( / ( * 2 2 ) 8 ) )"  output 16.5
input "1234" then shopuld get 1234.0

Invalid (+ 1 2 )
即所有token必须被一对space包围
"""

class Parser:
    def __init__(self, expr):
        self.tokens = expr.split() # 用(" ")而不是()来处理"(+ .replace('(', ' ( ').replace(')', ' ) ')
        # self.tokens = [_ for _ in self.tokens if _]
        self.current = 0 # current index

    def parse(self):
        if self.current >= len(self.tokens):
            raise SyntaxError("Unexpected end of expression")
        token = self.tokens[self.current]

        if token == '(':
            self.current += 1
            return self.parse_expression()
        elif token.isdigit():
            self.current += 1
            return float(token)

        else:
            print(f"token {token}")
            raise SyntaxError(f"Unexpected token: {token}")

    def parse_expression(self):
        op = self.parse_operator()
        args = []
        while self.current < len(self.tokens) and self.tokens[self.current] != ')':
            args.append(self.parse())
        if self.current >= len(self.tokens):
            raise SyntaxError("Expected ')' to close expression")
        self.current += 1  # consume ')'
        return op(*args)

    def parse_operator(self):
        if self.current >= len(self.tokens):
            raise SyntaxError("Expected operator")
        op = self.tokens[self.current]
        self.current += 1
        if op == '+':
            return lambda *args: sum(args)
        elif op == '-':
            return lambda *args: args[0] - sum(args[1:])
        elif op == '*':
            return lambda *args: args[0] * args[1]
        elif op == '/':
            return lambda *args: args[0] / args[1]
        else:
            raise SyntaxError(f"Unknown operator: {op}")


def evaluate(expression):
    parser = Parser(expression)
    return parser.parse()


# chatGPT生成一个简化版本

def evaluate2(expression):
    """递归"""
    tokens = expression.split()
    print(f"tokens: {tokens}")
    return evaluate_helper(tokens)[0]


def evaluate_helper(tokens):
    if tokens[0] == '(':
        op = tokens[1]
        left_operand, tokens = evaluate_helper(tokens[2:])
        right_operand, tokens = evaluate_helper(tokens)
        print(f"left {left_operand} right {right_operand}")
        if op == '+':
            return (left_operand + right_operand, tokens[1:])
        elif op == '-':
            return (left_operand - right_operand, tokens[1:])
        elif op == '*':
            return (left_operand * right_operand, tokens[1:])
        elif op == '/':
            return (left_operand / right_operand, tokens[1:])
    else:
        return (float(tokens[0]), tokens[1:])


# 150 逆波兰表达式

def evaluate_expression3(expression):
    """栈"""


    operators = { '+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y }

    stack = []
    tokens = expression.split()

    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token.isdigit():
            stack.append(float(token))
        elif token in operators:
            stack.append(token)
        elif token == ')':
            operand2 = stack.pop()
            operand1 = stack.pop()
            if operand1 == "(":
                raise ValueError(f"{tokens} is invalid")

            operator = stack.pop()
            if operator not in operators:
                raise ValueError(f"{operator} is invalid")

            assert stack.pop() == "(" # Remove the opening parenthesis
            func = operators[operator]
            if func == "/" and operand2 == 0:
                raise ValueError(f"{operand1} / {operand2} is invalid")
            result = func(operand1, operand2)
            stack.append(result)
        else:
            raise ValueError(f"{token} is invalid")
        # print(stack)
    return stack.pop()

# Test cases







"""
copied from the codepad

# "1234" -> 1234.0
# "( + 1 2 )" -> 3.0
# "( + ( * 1 2 ) 2 )" -> 4.0
# "( - ( + 15 2 ) ( / ( * 2 2 ) 8 ) )" -> 16.5

# Expr -> Int >= 0
# Expr -> ( Op Expr[0] Expr[1] )
# Op -> + - * /

# Expr[0] Op Expr[1]

# All expressions given will be valid
# INVALID: "( 12 )"
# INVALID: "(+ 1 2)"
# INVALID: "( / 1 0 )"


class Parser:
    def __init__(self, expr):
        self.tokens = expr.split(" ")
        self.current = 0 # current index
    
    def parse(self):
        if self.current >= len(self.tokens):
            raise SyntaxError
        token = self.tokens[self.current]

        if token == "(":
            self.current += 1
            return self.parse_expression()
        elif token.isdigit():
            self.current += 1
            return float(token)
        else:
            raise ValueError("Unexpected token")

    def parse_expression(self):
        op = self.parse_operator()
        args = []
        while self.current < len(self.tokens) and self.tokens[self.current] != ")":
            args.append(self.parse())
        if self.current >= len(self.tokens):
            raise SyntaxError("Expected ')'")
        self.current += 1
        return op(*args) # 

    def parse_operator(self):
        op = self.tokens[self.current]
        self.current += 1
        if op == "+":
            return lambda *args: sum(args)
        elif op == "-":
            return lambda *args: args[0] - sum(args[1:])
        elif op == "*":
            return lambda *args: args[0] * args[1]
        elif op == "/":
            return lambda *args: args[0] / args[1]
        

def calculate(expression: str) -> float:
    parser = Parser(expression)
    return parser.parse()    


inputs = ["( + 1 2 )", "( + ( * 1 2 ) 2 )","( - ( + 15 2 ) ( / ( * 2 2 ) 8 ) )" ]
for input in inputs:
    print(calculate(input))

print(calculate("1234"))

print(calculate("( + ( - ( * ( / 123 246 ) 4 ) 1 ) 0 )")) # => 1
print(calculate("( - ( + 15 2 ) ( / ( * ( + 23 3232 ) 2 ) 8 ) )")) # => -796.75

"""

if __name__ == "__main__":
# Test cases
    test_cases = [
        "1234",
        "( + 1 2 )",
        "( + ( * 1 2 ) 2 )",
        "( - ( + 15 2 ) ( / ( * 2 2 ) 8 ) )",
        "( + ( - ( * ( / 123 246 ) 4 ) 1 ) 0 )",
        "( - ( + 15 2 ) ( / ( * ( + 23 3232 ) 2 ) 8 ) )"
    ]

    for test_case in test_cases:
        result = evaluate_expression3(test_case)
        print(f"{test_case} -> {result}")

try:
    evaluate_expression3("( 12 )")
except:
    print("invalid")

try:
    evaluate_expression3("(+ 1 2 )")
except:
    print("invalid")

try:
    evaluate_expression3("( / 1 0 )")
except:
    print("invalid")



