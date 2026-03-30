class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        myDict = {')':'(', '}':'{', ']':'['} 

        for i in s:
            if i in myDict.values():
                stack.append(i)
            
            else:
                if len(stack) != 0:
                    if myDict[i] != stack.pop():
                        return False
                else:
                    return False
    
        if len(stack) == 0:
            return True
        else:
            return False



            