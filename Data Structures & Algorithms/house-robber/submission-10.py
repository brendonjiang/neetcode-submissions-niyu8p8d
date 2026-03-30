class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def helper(i):
            if i in memo:
                return memo[i]

            if i >= len(nums):
                return 0

            memo[i] = max(helper(i+1), nums[i] + helper(i+2))
            return memo[i]

        return helper(0)