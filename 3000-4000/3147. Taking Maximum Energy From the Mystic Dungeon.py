# Solution 1:
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        energy = energy[::-1]
        res = float('-inf')
        for idx in range(k):
            total = 0
            for nidx in range(idx, len(energy), k):
                total += energy[nidx]
                res = max(res, total)
        return res


# Solution 2:
# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/solutions/5145723/java-c-python-dp/
# dp[i] = A[i] + dp[i + k], where dp[i] is the energy starting at A[i]
# Instead of create an array for DP, we can also do it in-palce of A.

class Solution:
    def maximumEnergy(self, A: List[int], k: int) -> int:
        for i in range(len(A) - k - 1, -1, -1):
            A[i] += A[i + k]
        return max(A)

