class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        L, R = 0, len(heights)-1
        output = 0

        while L < R:
            area = (R-L)*min(heights[L], heights[R])
            output = max(output, area)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return output

    

            

