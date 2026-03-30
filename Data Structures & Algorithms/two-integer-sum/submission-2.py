class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        
        for i, j in enumerate(nums):
            complement = target - j
            if (complement in myMap):
                return [myMap[complement], i]
            myMap[j] = i
        
