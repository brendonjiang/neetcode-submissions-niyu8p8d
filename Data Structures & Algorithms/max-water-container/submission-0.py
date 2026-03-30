class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        for R in range(1, len(heights)):
            for L in range(0, R):
                area = min(heights[R], heights[L]) * (R-L)
                maxArea = max(maxArea, area)

        return maxArea


