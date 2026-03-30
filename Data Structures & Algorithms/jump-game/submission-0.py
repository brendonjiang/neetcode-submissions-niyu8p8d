class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach = False
        def helper(i):
            nonlocal canReach
            if i >= len(nums)-1:
                canReach = True
                return 

            for j in range(1, nums[i]+1):
                helper(i+j)

            return


        helper(0)
        return canReach