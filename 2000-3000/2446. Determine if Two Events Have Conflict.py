class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def convert(time):
            return int(time[0: 2]) * 60 + int(time[3: 5])
        
        starts = [convert(time) for time in [event1[0], event2[0]]]
        ends = [convert(time) for time in [event1[1], event2[1]]]
        
        return max(starts) <= min(ends)
