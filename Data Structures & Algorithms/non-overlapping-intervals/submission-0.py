class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda i:i[0])

        initial = len(intervals)

        prevEnd = intervals[0][1]
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if start < prevEnd:
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
                output.append([start, end])

        return (initial - len(output))