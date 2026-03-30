class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}

        for org, dest in prerequisites:
            adjList[org].append(dest)

        
        visits = set()
        def dfs(node):
            if node in visits:
                return False
            if adjList[node] == []:
                return True


            visits.add(node)
            for neighbor in adjList[node]:
                if not dfs(neighbor):
                    return False
                
            visits.remove(node)
            adjList[node] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False

        return True