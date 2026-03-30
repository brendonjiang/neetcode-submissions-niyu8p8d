class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def isPal(L, R, s):
            while L < R:
                if s[L] != s[R]:
                    return False

                L += 1
                R -= 1

            return True


        count = 0

        for i in range(len(s)):
            L, R = i, i
            while L >= 0 and R < len(s) and isPal(L, R, s):
                
                count += 1
                L -= 1
                R += 1

            L, R = i, i+1
            while L >= 0 and R < len(s) and isPal(L, R, s):
                
                count += 1
                L -= 1
                R += 1

        return count
