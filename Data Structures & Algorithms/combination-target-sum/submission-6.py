class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(i, total, curset):
            if total == target:
                res.append(curset.copy())
                return

            if i == len(nums) or total > target:
                return
            

            curset.append(nums[i])
            helper(i, total+nums[i], curset)
            curset.pop()
            helper(i+1, total, curset)

            return

        res = []

        helper(0, 0, [])

        return res            