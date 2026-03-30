class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone1, stone2 = heapq.heappop_max(stones), heapq.heappop_max(stones)

            if stone1 == stone2:
                continue
            elif stone1 < stone2:
                heapq.heappush_max(stones, stone2-stone1)
            else:
                heapq.heappush_max(stones, stone1-stone2)

        return stones[0] if stones else 0
