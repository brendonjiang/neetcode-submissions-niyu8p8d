class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}

        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        visits = set()
        count = 0
        def dfs(node):
            if node in visits:
                return

            visits.add(node)
            for neighbor in adjList[node]:
                dfs(neighbor)

            return

        for node, neighbors in adjList.items():
            if node not in visits:
                dfs(node)
                count += 1

        return count
        