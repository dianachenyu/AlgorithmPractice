class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        counter = collections.defaultdict(int)
        for num in nums:
            counter[(num - 1) % k + 1] += 1
        res = 0
        for rem1 in range(1, k + 1):
            min_rem2 = k // math.gcd(k, rem1)
            for rem2 in range(min_rem2, k + 1, min_rem2):
                if rem1 != rem2:
                    res += counter[rem1] * counter[rem2]
                else:
                    res += counter[rem1] * (counter[rem1] - 1)
        return res // 2 
        
