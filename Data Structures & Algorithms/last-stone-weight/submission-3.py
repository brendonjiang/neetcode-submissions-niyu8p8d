class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        minHeap = stones
        heapq.heapify_max(minHeap)

        while len(minHeap) >= 2:
            stone1 = heapq.heappop_max(minHeap)
            stone2 = heapq.heappop_max(minHeap)

            if stone1 != stone2:
                new_stone = abs(stone2 - stone1)
                heapq.heappush_max(minHeap, new_stone)

            else:
                continue

        return minHeap[0] if minHeap else 0
