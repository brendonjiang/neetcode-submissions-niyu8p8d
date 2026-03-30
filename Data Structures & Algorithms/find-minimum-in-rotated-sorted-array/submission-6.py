class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1


        while L < R:
            m = (L+R) // 2
            print(L, m, R, nums[L], nums[m], nums[R])
            if nums[L] < nums[m] and nums[m] > nums[R]:
                L = m

            elif nums[m] < nums[R] and nums[m] < nums[L]:
                R = m
            
            elif nums[L] < nums[m] and nums[m] < nums[R]:
                return nums[L]
            
            elif nums[L] == nums[m] and nums[R] > nums[m]:
                return nums[L]
            else:
                return nums[R]

        return nums[0]
            