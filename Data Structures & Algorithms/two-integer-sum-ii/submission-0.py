class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        myDict = {}
        for i, j in enumerate(numbers):
            targ = target-j
            if targ in myDict:
                return [myDict[targ]+1, i+1]
            myDict[j] = i


