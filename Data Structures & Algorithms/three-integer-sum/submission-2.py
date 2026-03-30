class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        mySet = set()

        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total > 0:
                    k -= 1

                elif total < 0:
                    j += 1

                else:
                    mySet.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1

        
        for tup in mySet:
            output.append(list(tup))

        return output
        