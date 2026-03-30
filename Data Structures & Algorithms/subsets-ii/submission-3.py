class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def helper(i, path):
            if i == len(nums):
                res.append(path.copy())
                return

        
            path.append(nums[i])
            helper(i+1, path)
            path.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            helper(i+1, path)


            return

        
        res = []
        helper(0, [])
        return res