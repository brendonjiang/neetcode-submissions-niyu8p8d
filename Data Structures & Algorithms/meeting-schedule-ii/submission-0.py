"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []

        for meeting in intervals:
            start.append(meeting.start)
            end.append(meeting.end)

        start.sort()
        end.sort()

        res = 0
        S, E, count = 0, 0, 0 

        while S < len(start):
            if start[S] < end[E]:
                count += 1
                S += 1
            else:
                count -= 1
                E += 1

            res = max(res, count)

        return res            