from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myDict = defaultdict(int)
        
        for num in nums:
            myDict[num] += 1

        counts = []
        for key, value in myDict.items():
            counts.append((value, key))

        heapq.heapify_max(counts)

        output = []
        for i in range(k):
            output.append(heapq.heappop_max(counts)[1])
            

        return output