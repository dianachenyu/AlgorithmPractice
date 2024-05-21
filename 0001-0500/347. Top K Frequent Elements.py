# Method 1:

# Time O(N + KlogN)
# Space O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        pairs = counter.most_common(k)
        return [pair[0] for pair in pairs]
        

# Method 2: Bucket Sort 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, freq in counter.items():
            buckets[freq].append(num)
        res = []
        for nums in buckets[::-1]:
            res.extend(nums)
            if len(nums) >= k:
                break
        return res[:k]
# Time O(N)
# Space O(N)
