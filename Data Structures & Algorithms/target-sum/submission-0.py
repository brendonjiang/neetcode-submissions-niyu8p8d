class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def helper(i, total):
            nonlocal counter 

            if i >= len(nums) and total == target:
                counter += 1
                return

            if i >= len(nums) and (total < target or total > target):
                return

            helper(i+1, total + nums[i])
            helper(i+1, total - nums[i])

            return


        counter = 0
        helper(0, 0)
        return counter