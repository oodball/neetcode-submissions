"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 1:
            return 1
        if not intervals:
            return 0
        
        starts = [interval.start for interval in intervals]
        ends = [interval.end for interval in intervals]

        starts.sort()
        ends.sort()

        overlap = 1
        count = []
        j = 0
        i = 1

        print(starts, ends)

        while i in range(len(starts)):
            print(i, j, overlap)
            if starts[i] >= ends[j]:
                overlap -= 1
                j += 1
            else:
                overlap += 1
                i += 1
            count.append(overlap)
        
        return max(count)