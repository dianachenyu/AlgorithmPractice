class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        pair = left = 0
        for num, count in counter.items():
            pair += count // 2
            left += count % 2
        return [pair, left]
        
