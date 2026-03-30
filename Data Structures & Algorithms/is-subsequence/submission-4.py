class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        
        
        if len(s) == 0:
            return True
        elif len(t) == 0 or len(t) < len(s):
            return False
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1

            if j == len(s):
                return True

            
        
        else:
            return False