
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adjList = {}

        for node1, node2 in edges:
            if node1 not in adjList:
                adjList[node1] = []

            if node2 not in adjList:
                adjList[node2] = []

            adjList[node1].append(node2)
            adjList[node2].append(node1)

        isValid = True

        def dfs(node, path, prev):
            nonlocal isValid

            if node in path:
                isValid = False
                return

            
            path.add(node)

            
            for neighbor in adjList[node]:
                if neighbor == prev:
                    continue
                dfs(neighbor, path, node)

            path.remove(node)

            return

        
        for src in adjList.keys():
            dfs(src, set(), None)

        return isValid 


        

        