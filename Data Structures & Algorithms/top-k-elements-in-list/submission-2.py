class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import defaultdict, Counter

        myCounts = defaultdict(int)


        for num in nums:
            myCounts[num] += 1

        freq = []
        for number, counts in myCounts.items():
            freq.append((counts, number))

        heapq.heapify_max(freq)

        output = []
        for _ in range(k):
            output.append(heapq.heappop_max(freq)[1])

        return output