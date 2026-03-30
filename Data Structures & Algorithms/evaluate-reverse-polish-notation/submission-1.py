import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        stack = []

        for char in tokens:
            if char in operators:
                char2 = stack.pop()
                char1 = stack.pop()
                stack.append(int(operators[char](char1, char2)))
            else:
                stack.append(int(char))

        return stack[0]