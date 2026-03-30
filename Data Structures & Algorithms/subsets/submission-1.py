class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums, cur, sub):
            if i >= len(nums):
                sub.append(cur.copy())
                return sub

            cur.append(nums[i])
            helper(i+1, nums, cur, sub)
            cur.pop()

            helper(i+1, nums, cur, sub)

            return sub
        cur, sub = [], []
        return helper(0, nums, cur, sub)