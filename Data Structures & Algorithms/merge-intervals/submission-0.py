class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        newarr = [intervals[0]]
        for start, end in intervals:
            prevend = newarr[-1][1]
            prevstart = newarr[-1][0]
            if start <= prevend:
                newarr[-1][1] = max(prevend, end)
                
            else:
                newarr.append([start, end])
        return newarr
        