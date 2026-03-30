class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key= lambda i : i[0])
        if not intervals:
            return [newInterval]
        output = []
        
        for start, end in intervals:
            if end < newInterval[0]:
                output.append([start, end])

        i = len(output)


        output.append(newInterval)

        for start, end in intervals[i:]:
            if start <= output[-1][1]:
                output[-1][1] = max(end, output[-1][1])
                output[-1][0] = min(start, output[-1][0])

            else:
                output.append([start, end])
    
        return output