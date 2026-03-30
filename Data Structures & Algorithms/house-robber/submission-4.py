class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def helper(i, total):
            if (i, total) in memo:
                return memo[(i, total)]

            if i >= len(nums):
                return total

            memo[(i, total)] = max(helper(i+1, total), helper(i+2, total + nums[i]))

            return memo[(i, total)]


        return helper(0, 0)