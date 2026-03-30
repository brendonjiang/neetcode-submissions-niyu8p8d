class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]
        for n in nums:
            count[n] += 1

        i = 0
        for j in range(len(count)):
            for k in range(count[j]):
                nums[i] = j
                i += 1

        
