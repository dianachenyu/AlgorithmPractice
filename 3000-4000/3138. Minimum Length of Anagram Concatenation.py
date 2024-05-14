from collections import Counter
class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for k in range(1, n):
            if n % k == 0:
                count1 = Counter(s[: k])
                for idx in range(k, n, k):
                    count2 = Counter(s[idx: idx+k])
                    if count1 != count2:
                        break
                else:
                    return k
        return n
      
