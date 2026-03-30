class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(curset):
            if len(curset) == len(nums):
                res.append(curset.copy())
                return

            for num in nums:
                if num not in curset:
                    curset.append(num)
                    helper(curset)
                    curset.pop()

                
            return

        
        res = []

        helper([])
        return res