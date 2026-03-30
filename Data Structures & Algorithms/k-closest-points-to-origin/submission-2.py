import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for x, y in points:
            distance = float(math.sqrt(x**2 + y**2))

            distances.append([distance, [x, y]])

        heapq.heapify(distances)
        output = []

        for i in range(k):
            output.append(heapq.heappop(distances)[1])

        return output
