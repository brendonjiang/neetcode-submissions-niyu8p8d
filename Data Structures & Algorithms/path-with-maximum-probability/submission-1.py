import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = {}
        longest = {}

        for i in range(n):
            adjList[i] = []

        for i in range(len(edges)):
            edges[i].append(succProb[i])
            

        for u, v, w in edges:
            adjList[u].append([v, w])
            adjList[v].append([u, w])


        maxHeap = [[1, start_node]]
        heapq.heapify_max(maxHeap)

        while maxHeap:
            w1, n1 = heapq.heappop_max(maxHeap)

            if n1 in longest:
                continue
            longest[n1] = w1

            for n2, w2 in adjList[n1]:
                if n2 not in longest:
                    heapq.heappush_max(maxHeap, [float(w1*w2), n2])

        if end_node not in longest.keys():
            return 0

        return longest[end_node]