class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def helper(i, curset, total):
            if total == target:
                res.append(curset.copy())
                return

            if i >= len(candidates) or total > target:
                return

            for j in range(i, len(candidates)):
                if candidates[j] == candidates[j-1] and j > i:
                    continue
                curset.append(candidates[j])
                helper(j+1, curset, total + candidates[j])
                curset.pop()
                


        res = []

        helper(0, [], 0)
        return res