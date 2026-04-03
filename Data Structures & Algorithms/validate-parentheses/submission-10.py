class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {")": "(", "]": "[", "}": "{"}

        stack = []

        for char in s:
            if stack and char in myDict.keys():
                if stack and stack[-1] != myDict[char]:
                    return False

                stack.pop()


            else:
                stack.append(char)

        return True if not stack else False