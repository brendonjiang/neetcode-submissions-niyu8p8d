class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def helper(i):
            if i in memo:
                return memo[i]
            
            if i >= len(s):
                return 1


            if s[i] == "0":
                return 0
                
            
            memo[i] = helper(i+1)
            if i < len(s)-1:
                if 10 <= int(s[i:i+2]) <= 26:
                    memo[i] += helper(i+2) 

            return memo[i]


        return helper(0)
        
            


            