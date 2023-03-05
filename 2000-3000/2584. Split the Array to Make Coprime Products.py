class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        MAX = 1000
        
        @functools.cache
        def get_primes(num):
            primes = set()
            for i in range(2, MAX + 1):
                while num % i == 0:
                    primes.add(i)
                    num //= i
            if num > 1:
                primes.add(num)
            return primes 
        
        # calculate the right most index of each prime
        idxs = collections.defaultdict(int)
        for idx, num in enumerate(nums):
            for factor in get_primes(num):
                idxs[factor] = idx
        
        #  for all primes scanned so far, their right most index
        right_most_idx = -1
        for idx, num in enumerate(nums[: -1]):
            for factor in get_primes(num):
                right_most_idx = max(right_most_idx, idxs[factor])
            # primes scanned so far do not exist in the right side 
            if right_most_idx == idx:
                return idx
        return -1
            
            
# Time O(NlogM), Space O(NlogM), N = len(nums), M = 1000
        
        
        
        
