class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        output = ""
        for i in range(len(s)):
            L, R = i, i
            ans = self.helper(L, R, s)
            if ans[0] > longest:
                longest = ans[0]
                output = ans[1]

            L, R = i, i+1
            ans = self.helper(L, R, s)
            if ans[0] > longest:
                longest = ans[0]
                output = ans[1]
                
        return output

    def helper(self, L, R, s):
        longest = 0
        output = ""
        while L >= 0 and R < len(s) and s[L] == s[R]:
            if (R-L+1) > longest:
                longest = R-L+1
                output = s[L:R+1]
            R += 1
            L -= 1

        return longest, output