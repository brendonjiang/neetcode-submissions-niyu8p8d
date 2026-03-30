class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mySet = {}

        for i in range(len(nums)):
            number = target - nums[i]

            if number in mySet:
                return [mySet[number], i]

            else:
                mySet[nums[i]] = i


        