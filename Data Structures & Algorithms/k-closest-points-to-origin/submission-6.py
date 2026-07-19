class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq, math

        coords = []
        heapq.heapify(coords)

        for x, y in points:
            dist = math.sqrt((x **2) + (y**2))
            heapq.heappush(coords, (dist, x, y))


        res = []
        for _ in range(k):
            point = heapq.heappop(coords)
            res.append([point[1], point[2]])

        return res
