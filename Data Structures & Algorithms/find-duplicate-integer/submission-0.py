class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mySet = {}

        for i in range(0, len(nums)):
            if nums[i] in mySet:
                return nums[i]

            mySet[nums[i]] = 1

             