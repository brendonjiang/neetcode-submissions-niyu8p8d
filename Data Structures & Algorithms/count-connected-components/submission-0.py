class DSU:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.par[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True


        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        dsu = DSU(n)
        res = n

        for x, y in edges:
            if dsu.union(x, y):
                res -= 1

        return res
        