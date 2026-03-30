class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s, L, R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1

            return True
        

        L, R = 0, len(s)-1

        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1

            else:
                return (helper(s, L+1, R) or helper(s, L, R-1))


        return True
