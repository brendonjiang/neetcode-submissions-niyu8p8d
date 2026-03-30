class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import heapq

        heap = []
        heapq.heapify(heap)

        for num in arr:
            point = [abs(x - num), num]
            heapq.heappush(heap, point)

        output = []
        for _ in range(k):
            output.append(heapq.heappop(heap)[1])

        return sorted(output)