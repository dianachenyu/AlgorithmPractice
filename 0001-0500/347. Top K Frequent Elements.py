# Method 1:

# Time O(nlogk)
# Space O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        pairs = counter.most_common(k)
        return [pair[0] for pair in pairs]
        

# Method 2:
# Time O(n)
# Space O(n)
