class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}

        def helper(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return True

            

            for end in range(start, len(s)):
                if s[start:end+1] in wordDict:
                    if helper(end+1):
                        memo[start] = True
                        return True
            
            memo[start] = False
            return False


        return helper(0)

            