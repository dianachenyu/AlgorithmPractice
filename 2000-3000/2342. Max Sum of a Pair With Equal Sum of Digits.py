class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        lookup = collections.defaultdict(list)
        
        def sum_digit(num):
            ssum = 0
            while num:
                ssum += num % 10
                num //= 10
            return ssum
        
        for num in nums:
            ssum = sum_digit(num)
            if len(lookup[ssum]) < 2:
                lookup[ssum].append(num)
            elif num > min(lookup[ssum]):
                lookup[ssum] = [max(lookup[ssum]), num]
        
        for pair in lookup.values():
            if len(pair) == 2:
                res = max(res, sum(pair))
        return res 
        
