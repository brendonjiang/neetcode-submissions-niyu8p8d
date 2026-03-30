import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            distance = math.sqrt((x**2) + (y**2))
            maxHeap.append((distance, x, y))

        heapq.heapify(maxHeap)

        output = []
        for i in range(k):
            cur = heapq.heappop(maxHeap)
            output.append([cur[1], cur[2]])

        return output