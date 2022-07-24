# Method 1
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        bits = [bin(num).count('1') for num in nums]
        bits.sort()
        
        N = len(counts)
        right = N - 1
        res = 0
        for left in range(N):
            while right >= 0 and count[left] + count[right] >= k:
                right -= 1
            res += N - 1 - right
        return res 

                                                        
# Method 2
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        counter = collections.Counter(num.bit_count() for num in nums)
        return sum(counter[i] * counter[j] for i in counter for j in counter if i + j >= k)
