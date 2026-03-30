from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        myList = defaultdict(list)

        for dst, src in prerequisites:
            myList[src].append(dst)

        visited = set()
        path = set()

        def dfs(node, visited, path):
            if node in path:
                return False
            
            if node in visited:
                return True

            path.add(node)

            for neighbors in myList[node]:
                if not dfs(neighbors, visited, path):
                    return False

            path.remove(node)
            visited.add(node)
            return True

        for c in range(numCourses):
            if not dfs(c, visited, path):
                return False

        return True


