class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        def helper(i, path):
            if i == len(nums):
                res.append(path.copy())
                return

            
            path.append(nums[i])
            helper(i+1, path)
            path.pop()
            helper(i+1, path)

            return

        res = []
        helper(0, [])
        return res