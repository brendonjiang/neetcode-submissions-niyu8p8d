class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def helper(i, curset):
            if i == len(nums):
                res.append(curset.copy())
                return


            curset.append(nums[i])
            helper(i+1, curset)
            curset.pop()
            helper(i+1, curset)
            return

        res = []
        helper(0, [])
        return res