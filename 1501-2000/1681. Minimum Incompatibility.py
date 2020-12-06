# Method 1: DP. n <= 16. at most 2^16 selections.
# optimization: keep ordering of duplicate numbers to reduce cases. eg. [1,2,1,4], always use the 1st 1 before the 2nd 1. 
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        N_PER_BUCKET = len(nums)//k
        
        @functools.lru_cache(None)
        def dp(nums):
            if not nums:
                return 0
            
            res = float('inf')
            for chosen_nums in itertools.combinations(set(nums), N_PER_BUCKET):
                nnums = list(nums)
                for chosen in chosen_nums:
                    nnums.remove(chosen)
                cost = dp(tuple(nnums)) + max(chosen_nums) - min(chosen_nums)
                res = min(res, cost)
            return res
           
        ans = dp(tuple(nums))
        return ans if ans < float('inf') else -1


# Method 2: DP + bitmask
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        N_PER_BUCKET = n//k
        
        @functools.lru_cache(None)
        def dp(mask):
            if mask == (1 << n) - 1:
                return 0
        
            res = float('inf')
            left_bits = [i for i in range(n) if not mask & (1 << i)]
            for bits in itertools.combinations(left_bits, N_PER_BUCKET):
                chosen_nums = [nums[-i-1] for i in bits]
                if len(set(chosen_nums)) < N_PER_BUCKET:
                    continue
                nmask = mask
                for i in bits:
                    nmask ^= (1 << i)
                cost = max(chosen_nums) - min(chosen_nums) + dp(nmask)
                res = min(res, cost)
            return res
           
        ans = dp(0)
        return ans if ans < float('inf') else -1
