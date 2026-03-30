class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = []
        if dst not in self.adjList:
            self.adjList[dst] = []

        self.adjList[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList and dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True
        else:
            return False
        

    def hasPath(self, src: int, dst: int) -> bool:
        validPath = False
        def dfs(node, visits):
            nonlocal validPath

            if node in visits:
                return
            
            if node == dst:
                validPath = True
                return 

            visits.add(node)

            for neighbor in self.adjList[node]:
                dfs(neighbor, visits)

            return

    
        dfs(src, set())
        return validPath

            

