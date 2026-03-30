class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(L, R, s):
            while L < R:
                if s[L] != s[R]:
                    return False
                
                L += 1
                R -= 1
        
            return True


        
        L, R = 0, len(s)-1

        while L < R:
            if s[L] != s[R]:
                return isPalindrome(L, R-1, s) or isPalindrome(L+1, R, s)

            L += 1
            R -= 1

        return True