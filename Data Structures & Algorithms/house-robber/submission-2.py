class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]


            memo[i] = max(nums[i] + helper(i+2), helper(i+1))

            return memo[i]


        memo = {}

        return helper(0)