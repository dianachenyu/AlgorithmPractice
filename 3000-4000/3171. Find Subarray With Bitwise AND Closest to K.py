class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = float('inf')
        dp1 = {}
        for num in nums:
            res = min(res, abs(num - k))
            dp2 = {num}
            for total in dp1:
                total &= num 
                res = min(res, abs(total - k))
                dp2.add(total)
            dp1 = dp2
        return res

