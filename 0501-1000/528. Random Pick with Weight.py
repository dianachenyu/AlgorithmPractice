import random
import bisect 
class Solution:

    def __init__(self, w: List[int]):
        self.presum = w
        for i in range(1, len(w)):
            self.presum[i] += self.presum[i - 1]
        
    def pickIndex(self) -> int:
        num = random.randrange(0, self.presum[-1])
        idx = bisect.bisect(self.presum, num)
        return idx 


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
