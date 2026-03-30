class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def isPalindrome(L, R, s):
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True


        if len(s) == 1:
            return s

        max_length = 1
        max_sequence = s[0]

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                R = j
                L = i

                if isPalindrome(L, R, s) and (R-L)+1 > max_length:
                    max_sequence = s[L:R+1]
                    max_length = R-L


        return max_sequence