class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(i, curcomb, output, n, k):
            if len(curcomb) == k:
                output.append(curcomb.copy())
                return
            if i > n:
                return


            curcomb.append(i)
            helper(i+1, curcomb, output, n, k)
            curcomb.pop()

            helper(i+1, curcomb, output, n, k)

        curcomb, output = [], []
        helper(1, curcomb, output, n, k)
        return output