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
        ends =[interval.end for interval in intervals]
        
        starts.sort()
        ends.sort()
        print(starts)
        print(ends)

        countarr = []
        currcount = 0
        i = 0
        j = 0

        while i in range(len(starts)):
            if starts[i] < ends[j]:
                currcount += 1
                countarr.append(currcount)
                i += 1
            elif starts[i] >= ends[j]:
                currcount -= 1
                countarr.append(currcount)
                j += 1
            
        return max(countarr)
            

        