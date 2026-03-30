import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
            for i in range(len(stones)):
                stones[i] = -stones[i]

            heapq.heapify(stones)

            while len(stones) > 1:
                if not stones:
                    return 0
                
                stone1 = -heapq.heappop(stones)
                stone2 = -heapq.heappop(stones)

                if stone1 == stone2:
                    continue
                else:
                    diff = max(stone1, stone2) - min(stone1, stone2)
                    heapq.heappush(stones, -diff)
            if not stones:
                return 0
            return -stones[0]

