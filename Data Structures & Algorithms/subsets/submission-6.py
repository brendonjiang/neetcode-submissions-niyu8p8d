class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def helper(i, curset):
            if i == len(nums):
                res.append(curset.copy())
                return

            curset.append(nums[i])
            helper(i+1, curset)
            curset.pop()
            helper(i+1, curset)

            return res

        return helper(0, [])