class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(i, curcomb, output, n, k):
            if len(curcomb) == k:
                output.append(curcomb.copy())
                return
            if i > n:
                return


            for j in range(i, n+1):
                curcomb.append(j)
                helper(j+1, curcomb, output, n, k)
                curcomb.pop()

        curcomb, output = [], []
        helper(1, curcomb, output, n, k)
        return output