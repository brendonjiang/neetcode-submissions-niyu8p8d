class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def helper(i, total):
            if (i, total) in memo:
                return memo[(i, total)]

            if i == len(nums) and total == target:
                return 1

            elif i == len(nums) and (total < target or total > target):
                return 0
            
            memo[(i, total)] = helper(i+1, total + nums[i]) + helper(i+1, total - nums[i])
            return memo[(i, total)]

        
        return helper(0, 0)