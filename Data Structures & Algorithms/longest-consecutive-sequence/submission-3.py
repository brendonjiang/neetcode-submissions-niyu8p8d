import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heapq.heapify(nums)
        max_length = 0
        length = 1
        prev = heapq.heappop(nums)
        while nums:
            cur = heapq.heappop(nums)
            if prev+1 == cur:
                length += 1
            elif prev == cur:
                prev = cur
                continue
                
            else:
                max_length = max(length, max_length)
                length = 1
            prev = cur

        return max(max_length, length)
            




        