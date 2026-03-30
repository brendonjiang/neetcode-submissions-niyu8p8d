class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  
        maxArea = heights[0]

        for index, value in enumerate(heights):
            stored_index = index

            while stack and value < stack[-1][1]:
                area = (index-stack[-1][0])*stack[-1][1]
                maxArea = max(maxArea, area)
                stored_index = stack[-1][0]

                stack.pop()



            stack.append((stored_index, value))

        if stack:
            index = len(heights)
            while stack:
                area = (index-stack[-1][0])*stack[-1][1]
                maxArea = max(maxArea, area)
                stack.pop()


        return maxArea