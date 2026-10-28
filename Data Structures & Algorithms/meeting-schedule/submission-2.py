"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        starts = [int(interval.start) for interval in intervals]
        ends = [int(interval.end) for interval in intervals]
        starts.sort()
        ends.sort()

        print(starts)
        print(ends)

        i = 1
        j = 0

        while i in range(len(starts)):
            if starts[i] < ends[j]:
                return False
            i += 1
            j += 1    
        return True
