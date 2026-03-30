class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums, curset, subset):
            if i == len(nums):
                subset.append(curset.copy())
                return subset

            curset.append(nums[i])
            helper(i+1, nums, curset, subset)
            curset.pop()

            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1

            helper(i+1, nums, curset, subset)


        nums.sort()
        curset, subset = [], []
        helper(0, nums, curset, subset)
        return subset 