class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        import heapq, math

        minHeap = []

        for x, y in points:
            distance = (math.sqrt(x**2 + y**2))
            minHeap.append((distance, x, y))

        heapq.heapify(minHeap)

        output = []
        for _ in range(k):
            distance, x, y = heapq.heappop(minHeap)

            output.append([x, y])

        return output

        