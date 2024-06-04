class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        i = 0
        used = False
        while i < n or not used:
            if used or (i < n and intervals[i][0] < newInterval[0]):
                cur = intervals[i]
                i += 1
            else:
                cur = newInterval
                used = True
            if res and cur[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], cur[1])
            else:
                res.append(cur)
        return res

