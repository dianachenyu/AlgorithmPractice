class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = set()
        n = len(nums)
            
        for start in range(n): 
            count = 0
            for end in range(start, n):
                count += nums[end] % p == 0 
                if count > k:
                    break
                res.add(tuple(nums[start : end + 1]))
        return len(res)
                
        
