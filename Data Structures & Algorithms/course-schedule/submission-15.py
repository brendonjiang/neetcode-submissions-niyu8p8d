class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adjList[prereq].append(course)
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

            adjList[node] = []
            visits.remove(node)
            return True

        
        for node, neighbors in adjList.items():
            if not dfs(node):
                return False

        return True