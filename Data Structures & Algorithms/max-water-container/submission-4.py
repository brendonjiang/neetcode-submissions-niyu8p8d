class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        maxArea = 0

        while L < R:
            area = min(heights[L], heights[R]) * (R-L)
            maxArea = max(maxArea, area)

            if heights[L] <= heights[R]:
                L += 1

            elif heights[R] < heights[L]:
                R -= 1

            
    
        return maxArea