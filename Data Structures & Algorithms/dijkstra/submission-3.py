import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        adjList = {}

        for i in range(0, n):
            adjList[i] = []

        
        for u, v, w in edges:
            adjList[u].append([v, w])

        minHeap = [[0, src]]
        heapq.heapify(minHeap)
        shortest = {}

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in shortest:
                continue

            shortest[n1] = w1

            for n2, w2 in adjList[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1+w2, n2])

        for i in range(n):
            if i not in shortest.keys():
                shortest[i] = -1
        return shortest

    
