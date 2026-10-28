class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        if not intervals:
            output.append(newInterval)
            return output


        intervals.append(newInterval)
        intervals.sort()
        output.append(intervals[0])

        print(intervals)

        for start, end in intervals:
            prevstart = output[-1][0]
            prevend = output[-1][1]
            print(prevstart, prevend, start, end)

            if start <= prevend:
                output[-1][1] = max(prevend, end)
            else:
                output.append([start,end])
            print(output)
        return output