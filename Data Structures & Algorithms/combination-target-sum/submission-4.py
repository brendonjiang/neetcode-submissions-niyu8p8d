class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def helper(i, curset, total):
            if total == target:
                res.append(curset.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            
            curset.append(nums[i])
            helper(i, curset, total + nums[i])
            curset.pop()

            helper(i+1, curset, total)

        res = []
        helper(0, [], 0)
        return res        