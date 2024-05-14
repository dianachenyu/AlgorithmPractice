class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        MOD = 10 ** 9 + 7
        target = max(nums)
        n = len(nums)
        total = n * target - sum(nums)
        if 2 * cost1 <= cost2 or n <= 2:
            return total * cost1 % MOD
        
        q = target - min(nums)
        l = total - q

        if q <= l:
            # all numbers can pair and use cost2
            if total % 2 == 0:
                return total // 2 * cost2 % MOD
            else:
                res = total // 2 * cost2 + cost1
                if n % 2 == 1:
                    total += n
                    res = min(res, total // 2 * cost2)  
                return res % MOD
        else: # q > l
            # first, make l pairs to use cost2
            res = l * cost2
            q -= l 
            l = 0
            # Option1: apply cost1
            # Option2: increase target to apply cost2
            if cost2 * (n - 1) <= cost1 * (n - 2):
                # option 2 is cheaper
                j = q // (n -2)
                q = q % (n - 2)
                res += j * (n - 1) * cost2
            else:
                j = q // (n - 1)
                q = q % (n - 1)
                res += j * (n - 1) * cost1

            # now q < n - 1, decide use option 1 or 2 for the remaining q
            if q:
                op1 = q * cost1 

                j = (q + n) // 2
                q = (q + n) % 2
                op2 = j * cost2 + q * cost1
                if q % 2 and n % 2:
                    op2 = j * cost2 + min(q * cost1, (q + n) // 2 * cost2)
                res += min(op1, op2)
        return res % MOD


