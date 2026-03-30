import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        shortest = {}

        for i in range(1, n+1):
            adjList[i] = []

        for u, v, t in times:
            adjList[u].append([v, t])

        minHeap = [[0, k]]
        heapq.heapify(minHeap)

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in shortest:
                continue

            shortest[n1] = w1

            for n2, w2 in adjList[n1]:
                heapq.heappush(minHeap, [w1+w2, n2])
        
        for i in range(1, n+1):
            if i not in shortest.keys():
                return -1

        return max(shortest.values())