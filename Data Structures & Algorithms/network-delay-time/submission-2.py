import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        shortest = {}

        for ui, vi, ti in times:
            if ui not in adjList:
                adjList[ui] = []
            if vi not in adjList:
                adjList[vi] = []

            adjList[ui].append([vi, ti])

        
        minHeap = [[0, k]]
        heapq.heapify(minHeap)
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in shortest:
                continue

            shortest[n1] = w1

            for n2, w2 in adjList[n1]:
                heapq.heappush(minHeap, [w1+w2, n2])

        if len(shortest) != n:
            return -1

        else:
            return max(shortest.values())