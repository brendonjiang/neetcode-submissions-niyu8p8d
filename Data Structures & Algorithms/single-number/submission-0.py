from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        for num in nums:
            hash[num] += 1
            if hash[num] == 2:
                hash.pop(num)

        

        return list(hash.keys())[0]

        