class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = [0, 0, 0]


        for val in nums:
            colors[val] += 1
        
        i = 0
        for j in range(len(colors)):
            for k in range(colors[j]):
                nums[i] = j
                i += 1

            

        