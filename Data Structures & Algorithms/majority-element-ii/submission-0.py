from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        myDict = defaultdict(int)

        for num in nums:
            myDict[num] += 1

        majority = int(len(nums)/3)
        output = []

        for num, counts in myDict.items():
            if counts > majority:
                output.append(num)

        return output