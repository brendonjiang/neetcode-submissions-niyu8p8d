class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        for dst, src in prerequisites:
            if src not in adjList:
                adjList[src] = []
            if dst not in adjList:
                adjList[dst] = []

            adjList[src].append(dst)

        validPath = True
        def dfs(node, visits):
            nonlocal validPath

            if node in visits:
                validPath = False
                return

            
            visits.add(node)
            
            for neighbor in adjList[node]:
                dfs(neighbor, visits)
            visits.remove(node)
            adjList[node].clear()
            return

        for src in adjList.keys():
            dfs(src, set())

        return validPath
        
        