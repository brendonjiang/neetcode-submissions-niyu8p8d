"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals or len(intervals) == 1:
            return True

        intervals.sort(key= lambda i : i.start)
        prevEnd = intervals[0].end
        for meeting in intervals[1:]:
            if meeting.start < prevEnd:
                return False
            else:
                prevEnd = meeting.end

        return True
