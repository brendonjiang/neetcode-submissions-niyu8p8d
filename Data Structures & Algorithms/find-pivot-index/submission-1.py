class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        
        for num in nums:
            total += num
            prefix.append(total)

        
        for i in range(0, len(nums)):
            leftSum = prefix[i-1] if i > 0 else 0
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i

        return -1


       



