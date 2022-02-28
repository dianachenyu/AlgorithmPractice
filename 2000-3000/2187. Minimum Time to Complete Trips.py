class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def calculate(ttime):
            res = 0
            for t in time:
                res += ttime//t
            return res >= totalTrips
        
        left = 1
        right = min(time) * totalTrips
        while left < right:
            mid = (left + right) // 2
            if calculate(mid):
                right = mid
            else:
                left = mid + 1
        return left 
            
