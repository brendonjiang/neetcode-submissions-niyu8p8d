class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        def reverse(L, R, nums):
            while L < R:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
                R -= 1

            


        
        reverse(0, len(nums)-1, nums)
        reverse(0, k % len(nums) -1, nums)
        reverse(k % len(nums), len(nums)-1, nums)

        