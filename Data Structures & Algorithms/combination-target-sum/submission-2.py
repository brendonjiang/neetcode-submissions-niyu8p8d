class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        def helper(i, path, total):
            if total == target:
                res.append(path.copy())
                return

            if i >= len(nums) or total > target:
                return


            path.append(nums[i])
            helper(i, path, total + nums[i])
            path.pop()
            helper(i+1, path, total)

            return


        res = []
        helper(0, [], 0)
        return res
