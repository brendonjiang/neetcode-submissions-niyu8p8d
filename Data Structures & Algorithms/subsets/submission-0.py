class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums, curset, subset):
            if i == len(nums):
                subset.append(curset.copy())
                return subset
                
            curset.append(nums[i])
            helper(i+1, nums, curset, subset)

            curset.pop()
            helper(i+1, nums, curset, subset)
            
        subset, curset = [], []
        helper(0, nums, curset, subset)
        return subset


        
