class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        visits, cycle = set(), set()

        def dfs(node):
            if node in cycle:
                return False
            if node in visits:
                return True

            cycle.add(node)
            for neighbor in adjList[node]:
                if not dfs(neighbor):
                    return False
            cycle.remove(node)
            visits.add(node)
            output.append(node)
            return True

        output = []
        for crs in range(numCourses):
            if not dfs(crs):
                return []
            

        return output