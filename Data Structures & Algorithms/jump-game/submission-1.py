class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        
        def helper(i):
            if i in memo:
                return memo[i]

            if i >= len(nums)-1:
                return True

            for j in range(1, nums[i]+1):
                if helper(i+j):
                    memo[i] = True
                    return True

                
            memo[i] = False



            return memo[i]


        
        return helper(0)