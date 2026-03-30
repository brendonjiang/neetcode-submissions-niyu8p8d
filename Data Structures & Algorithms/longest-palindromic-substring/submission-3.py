class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        longest = 0

        for i in range(len(s)):
            L, R = i, i

            while L > -1 and R < len(s) and s[L] == s[R]:
                if R-L+1 > longest:
                    longest = R-L+1
                    output = s[L:R+1]
                R += 1
                L -= 1

            L, R = i, i+1
            
            while L > -1 and R < len(s) and s[L] == s[R]:
                if R-L+1 > longest:
                    longest = R-L+1
                    output = s[L:R+1]
                R += 1
                L -= 1
        return output