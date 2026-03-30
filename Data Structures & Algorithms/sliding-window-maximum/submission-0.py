class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return [max(nums)]

        myWindow = {}

        for i in range(k):
            myWindow[i] = nums[i]

        output = []

        output.append(max(myWindow.values()))
        
        L = 0
        for R in range(k, len(nums)):
            myWindow[R] = nums[R]
            myWindow.pop(L)
            L += 1
            output.append(max(myWindow.values()))


        return output
        


