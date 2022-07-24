class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rcounter = collections.Counter(map(tuple, grid))
        ccounter = collections.Counter(zip(*grid))
        return sum(rcounter[key] * ccounter[key] for key in rcounter)
      
