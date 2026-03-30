class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):
        
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        self.k = k

        for _ in range(len(nums)-self.k):
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
