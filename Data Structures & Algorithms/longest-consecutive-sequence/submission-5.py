class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)

        max_length = 0
        for num in nums:
            if num-1 not in mySet:
                length = 1

                while num+1 in mySet:
                    num = num+1
                    length += 1

                max_length = max(length, max_length)


        return max_length
                