class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest = 0

        for num in nums:
        
            if num-1 not in mySet:
                cur = 1

            
                while num+1 in mySet:
                    num += 1
                    cur += 1
            
                longest = max(cur, longest)

        return longest

            