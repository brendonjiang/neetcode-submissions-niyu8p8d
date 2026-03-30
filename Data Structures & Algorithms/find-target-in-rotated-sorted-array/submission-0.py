class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bst(nums, target, L, R):

            while L <= R:
                m = (L+R) // 2
                if target < nums[m]:
                    R = m-1
                elif target > nums[m]:
                    L = m+1

                else:
                    return m
            return -1

        L, R = 0, len(nums)-1

        while L <= R:
            m = (L+R) // 2

            if nums[m] >= nums[L] and nums[L] <= target <= nums[m]:
                return bst(nums, target, L, m)
            
            elif nums[m] <= nums[R] and nums[m] <= target <= nums[R]:
                return bst(nums, target, m, R)

            elif nums[m] >= nums[L]:
                L = m+1
            
            else:
                R = m-1

        return -1
            

                
