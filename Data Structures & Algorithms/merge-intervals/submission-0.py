class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        pos = 1
        res = []

        while pos < len(intervals):
            if intervals[pos][0] <= end:
                start = min(intervals[pos][0], start)
                end = max(intervals[pos][1], end)
            else:
                res.append([start, end])
                start = intervals[pos][0]
                end = intervals[pos][1]
            pos += 1
        
        res.append([start, end])
        return res     