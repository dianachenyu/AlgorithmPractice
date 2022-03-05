class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        withi = withouti = 0
        counter = collections.Counter(nums)
        for i in range(1, max(counter) + 1):
            withi, withouti = withouti + i * counter[i] if i in counter else 0, max(withi, withouti)
        return max(withi, withouti)
