class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max, suffix_max = 0, 0
        prefix, suffix = [], []

        for val in height: 
            prefix_max = max(prefix_max, val)
            prefix.append(prefix_max)

        for val in reversed(height):
            suffix_max = max(suffix_max, val)
            suffix.append(suffix_max)

        suffix.reverse()

        total = 0
    
        for i in range(len(height)):
            cur_trap = min(prefix[i], suffix[i]) - height[i]
            total += cur_trap

        return total