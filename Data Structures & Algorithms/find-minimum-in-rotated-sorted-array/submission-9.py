class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1
        min_value = 1001

        while L <= R:
            m = (L+R) // 2
            min_value = min(min_value, nums[m])
            min_value = min(min_value, nums[L])

            if nums[m] >= nums[L]:
                L = m+1

            else:
                R = m-1

        return min_value