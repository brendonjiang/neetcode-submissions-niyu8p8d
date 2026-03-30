class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}

        for src, dst in prerequisites:
            adjList[src].append(dst)


        visits = set()

        def dfs(node):
            if node in visits:
                return False

            visits.add(node)

            for neighbor in adjList[node]:
                if not dfs(neighbor):
                    return False
            adjList[node] = []
            visits.remove(node)
            return True


        for course, neighbors in adjList.items():
            if not dfs(course):
                return False

        return True
