class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        # the worst case is: fi = 1, ri = 2, changeTime = 10 ** 5
        # at most 18 laps without changing tire 
        one_tire = [0] * 19
        seconds = [0] * len(tires)
        for i in range(1, 19):
            for j in range(len(tires)):
                seconds[j] += tires[j][0] * tires[j][1] ** (i - 1)
            one_tire[i] = min(seconds)
                
        dp = [float('inf')] * (numLaps + 1)
        dp[0] = -changeTime
            
        for i in range(1, numLaps + 1):
            for j in range(1, min(i + 1, 19)):
                dp[i] = min(dp[i], dp[i - j] + changeTime + one_tire[j])
        return dp[-1]
      
# m = len(tires) n = numLaps
# Time O(m+n) Space O(m+n)
