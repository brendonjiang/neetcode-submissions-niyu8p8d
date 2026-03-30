import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest = {}
        adjList = {}

        for i in range(1, n+1):
            adjList[i] = []

        for ui, vi, ti in times:
            adjList[ui].append([vi, ti])

        minHeap = [[0, k]]
        heapq.heapify(minHeap)

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)

            if n1 in shortest:
                continue

            shortest[n1] = t1

            for n2, t2 in adjList[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [t2+t1, n2])


        for i in range(1, n+1):
            if i not in shortest.keys():
                return -1

        return max(shortest.values())