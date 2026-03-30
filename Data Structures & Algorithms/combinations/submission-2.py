class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        curset, combs = [], []

        def helper(i, curset, combs, n, k):
            if len(curset) == k:
                combs.append(curset.copy())
                return
            
            if i > n:
                return

            
            for i in range(i, n+1):
                curset.append(i)
                helper(i+1, curset, combs, n, k)
                curset.pop()


            
        helper(1, curset, combs, n, k)
        return combs