class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0

        def isPal(L, R, s):
            while L < R:
                if s[L] != s[R]:
                    return False

                L += 1
                R -= 1
            return True

        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPal(i, j, s):
                    count += 1


        return count