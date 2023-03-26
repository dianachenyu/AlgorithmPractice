class Solution:
    # Algorithm Sieve of Eratosthenes, find all prime numbers up to N
    def sieve(self, n):
        primes = [1] * (n + 1)
        primes[0] = primes[1] = 0
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = 0
        return [idx for idx in range(n + 1) if primes[idx]]
                
    # search for the largest prime smaller than nums[i] - nums[i - 1]
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = self.sieve(1000)
        for idx, num in enumerate(nums):
            prev = 0 if idx == 0 else nums[idx - 1]
            if num <= prev:
                return False 
            j = bisect.bisect_left(primes, num - prev)
            j -= 1
            if j >= 0:
                nums[idx] -= primes[j]
        return True 
    
    
# Greedy
# Time: O(n), n=len(nums). assume the number of primes within limit is constant.
