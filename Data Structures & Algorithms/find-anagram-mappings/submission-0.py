from collections import defaultdict
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myMap = defaultdict(list)

        for i in range(len(nums2)):
            myMap[nums2[i]].append(i)


        output = []

        for num in nums1:
            output.append(myMap[num].pop())

        return output