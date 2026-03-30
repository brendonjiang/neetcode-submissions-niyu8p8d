import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            d2o = float(math.sqrt(x**2+y**2))
            distances.append([d2o, x, y])

        heapq.heapify(distances)

        output = []
        for i in range(k):
            cur = heapq.heappop(distances)
            output.append([cur[1], cur[2]])

        return output
            



        