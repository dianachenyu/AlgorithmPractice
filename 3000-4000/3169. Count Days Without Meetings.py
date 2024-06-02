class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        res = 0
        meetings.sort()
        lend = 0
        for start, end in meetings:
            if start > lend:
                res += start - lend - 1
            lend = max(lend, end)
        res += days - lend
        return res 

