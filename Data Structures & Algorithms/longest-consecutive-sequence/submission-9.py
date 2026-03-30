class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)

        max_length = 0

        for num in nums:
            if num-1 not in mySet:
                length = 1

                while num + 1 in mySet:
                    length += 1
                    num += 1

                max_length = max(max_length, length)

        
        return max_length
