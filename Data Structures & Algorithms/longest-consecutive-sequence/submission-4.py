import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in mySet:
                length = 1
                while (num+length) in mySet:
                    length += 1

                longest = max(length, longest)


        return longest




        