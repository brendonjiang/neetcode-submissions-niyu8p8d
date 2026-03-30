class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mySet = set()

        for num in nums:
            mySet.add(num)

        for i in range(len(nums)+1):
            if i not in mySet:
                return i

        

        