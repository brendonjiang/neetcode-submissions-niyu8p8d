class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {}
        for num in nums:
            if num in myDict:
                return True
            myDict[num] = 1

        return False