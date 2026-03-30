class Solution:
    def isValid(self, s: str) -> bool:
        pars = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for char in s:
            if char in pars.keys():
                stack.append(char)

            else:
                if stack and pars[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        return True if not stack else False