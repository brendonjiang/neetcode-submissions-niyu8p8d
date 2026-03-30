import math
class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        mySet = {"+", "-", "/", "*"}
        for char in tokens:
            if char in mySet:
                y = stack.pop()
                x = stack.pop()

                if char == "+":
                    val = x + y

                elif char == "-":
                    val = x-y

                elif char == "/":
                    val = int(x/y)
                    print(val)


                else:
                    val = x*y
                print(val)
                stack.append(val)
            
            else:
                stack.append(int(char))

        
        return stack[0]
            
        