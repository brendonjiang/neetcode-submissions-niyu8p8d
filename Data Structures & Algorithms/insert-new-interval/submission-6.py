class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    
        output = []

        for start, end in intervals:
            if end < newInterval[0]:
                output.append([start, end])

        length = len(output)

        output.append(newInterval)

        for start, end in intervals[length:]:
            if start <= output[-1][1]:
                newStart = min(start, output[-1][0])
                newEnd = max(end, output[-1][1])

                output[-1] = [newStart, newEnd]

            else:
                output.append([start, end])


        return output
