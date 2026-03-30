class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        minHeap = nums
        heapq.heapify_max(minHeap)

        for _ in range(k-1):
            heapq.heappop_max(minHeap)

        return minHeap[0]