class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_value = len(nums) + 1

        

        for i in range(1, max_value+1):
            if i not in nums:
                return i

            