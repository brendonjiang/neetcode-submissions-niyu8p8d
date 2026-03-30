import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify_max(distances)

        for x, y in points:
            distance = math.sqrt(x**2+y**2)

            if len(distances) < k:
                heapq.heappush_max(distances, [distance, [x, y]])

            elif distance < distances[0][0]:
                heapq.heappop(distances)
                heapq.heappush(distances, [distance, [x, y]])

            
        
        return [i[1] for i in distances]

