class Solution:
    def rob(self, nums: List[int]) -> int:
        
        nums1 = nums[:-1]
        nums2 = nums[1:]

        memo = {}
        def helper(i, nums):
            if i in memo:
                return memo[i]

            if i >= len(nums):
                return 0

            memo[i] = max(helper(i+1, nums), nums[i]+helper(i+2, nums))
        
            return memo[i]

        if len(nums) == 1:
            return nums[0]
        
        max1 = helper(0, nums1)
        
        memo.clear()

        max2 = helper(0, nums2)


        return max(max1, max2)