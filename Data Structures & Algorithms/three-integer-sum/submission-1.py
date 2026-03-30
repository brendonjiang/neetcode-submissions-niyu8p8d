class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            j, k = i+1, len(nums)-1
            while j < k:
                total = nums[j] + nums[k]
                target = -nums[i]

                if total > target:
                    k -= 1
                
                elif total < target:
                    j += 1
                
                else:
                    output.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        final = []
        for x, y, z in output:
            final.append([x, y, z])
        return final
