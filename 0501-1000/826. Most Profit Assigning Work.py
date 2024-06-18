class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pairs = sorted(zip(profit, difficulty), reverse=True)
        worker.sort(reverse=True)
        res = 0
        n = len(pairs)
        m = len(worker)
        i = j = 0
        while i < n and j < m:
            while j < m and worker[j] >= pairs[i][1]:
                res += pairs[i][0]
                j += 1
            i += 1
        return res 
        
