class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}

        for i in range(0, n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return True
        else:
            return False

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)

        if p1 != p2:
        
            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
                
            
            elif self.rank[p2] > self.rank[p1]:
                self.par[p1] = p2

            else:
                self.par[p1] = p2
                self.rank[p2] += 1
            return True
        return False
    def getNumComponents(self) -> int:
        roots = set()

        for root in self.par:
            roots.add(self.find(root))

        return len(roots)
