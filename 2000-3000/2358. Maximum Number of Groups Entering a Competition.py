# Method 1:
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        k = 0
        while n >= k + 1:
            k += 1
            n -= k
        return k
 

# Method 2:     
# k * (k + 1) // 2 <= n
# (k + 0.5) ^ 2 <= 2n + 0.25
# k <= sqrt(2n + 0.25) - 0.5

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        return int(math.sqrt(2 * n + 0.25) - 0.5)
