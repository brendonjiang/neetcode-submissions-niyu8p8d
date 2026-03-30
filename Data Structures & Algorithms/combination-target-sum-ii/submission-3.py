class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(i, curset, total):
            if total == target:
                res.append(curset.copy())
                return

            if total > target or i >= len(candidates):
                return

            
        
            curset.append(candidates[i])
            helper(i+1, curset, total + candidates[i])
            curset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            helper(i+1, curset, total)

        
        candidates.sort()
        res = []
        helper(0, [], 0)
        return res