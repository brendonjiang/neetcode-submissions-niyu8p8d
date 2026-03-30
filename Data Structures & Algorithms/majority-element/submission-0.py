from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myMap = defaultdict(int)
        target = len(nums)/2
        for num in nums:
            myMap[num] += 1
            if myMap[num] > target:
                return num

            