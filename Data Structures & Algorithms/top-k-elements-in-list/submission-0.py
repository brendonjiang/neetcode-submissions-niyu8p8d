from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        myDict = dict(cnt)
        sortedList = sorted(myDict.items(), key=lambda x: x[1], reverse=True)
        return [sortedList[x][0] for x in range(k)]