class Graph:
    
    def __init__(self):
        self.adjList = defaultdict(list)

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = []
        if dst not in self.adjList:
            self.adjList[dst] = []

        self.adjList[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList and dst in self.adjList:
            self.adjList[src].remove(dst)
            return True

        else:
            return False

    def hasPath(self, src: int, dst: int) -> bool:
        def dfs(node, visits):
            if node == dst:
                return True

            if node in visits:
                return

            for neighbor in self.adjList[node]:
                if dfs(neighbor, visits):
                    return True

            return False

        return dfs(src, set())
