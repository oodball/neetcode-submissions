"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if intervals is None or len(intervals)== 1:
            return True
        starts = [interval.start for interval in intervals]
        ends = [interval.end for interval in intervals]
        starts.sort()
        ends.sort()

        i = 1
        j  = 0

        while i < len(starts):
            if starts[i] < ends[j]:
                return False
            i += 1
            j += 1
        return True