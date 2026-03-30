class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adjList = {}

        for i in range(1, n+1):
            adjList[i] = 0


        for src, dst in trust:
            adjList[dst] += 1
            adjList[src] -= 1


        for key, value in adjList.items():
            if value == n-1:
                return key

        return -1

        