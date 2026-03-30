class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def helper(i, curset):
            if i == len(nums):
                res.append(curset.copy())
                return

            
            curset.append(nums[i])
            helper(i+1, curset)
            curset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            helper(i+1, curset)
            
        res = []
        nums.sort()
        helper(0, [])
        return res