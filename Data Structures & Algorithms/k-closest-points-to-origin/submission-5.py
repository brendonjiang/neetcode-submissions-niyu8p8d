import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxHeap = []

        heapq.heapify(maxHeap)

        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(maxHeap, (distance, x, y))

        output = []
        for _ in range(k):
            point = heapq.heappop(maxHeap)
            output.append([point[1], point[2]])
            

        return output