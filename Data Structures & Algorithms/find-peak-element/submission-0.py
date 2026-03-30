class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_num = float("-inf")

        for i in range(len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
                output = i

        return output
