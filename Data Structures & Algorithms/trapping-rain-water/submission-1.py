class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, suffix = [], []
        maxHeight = 0

        for val in height:
            maxHeight = max(maxHeight, val)
            prefix.append(maxHeight)

        maxHeight = 0
        for val in reversed(height):
            maxHeight = max(maxHeight, val)
            suffix.append(maxHeight)
        suffix.reverse()

        total = 0

        for i in range(len(height)):
            total += min(prefix[i], suffix[i]) - height[i]


        return total