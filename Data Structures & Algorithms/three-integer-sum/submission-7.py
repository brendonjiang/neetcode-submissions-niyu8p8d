class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()


        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L, R = i+1, len(nums)-1
            while L < R:
                total = nums[L] + nums[R]

                if total > -nums[i]:
                    R -= 1

                elif total < -nums[i]:
                    L += 1

                else:
                    output.add((nums[i], nums[L], nums[R]))
                    R -=1
                    L += 1


        return [list(element) for element in output]
            
