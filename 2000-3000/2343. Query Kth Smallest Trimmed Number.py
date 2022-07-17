class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        m = len(queries)
        res = [0] * m
        lookup = collections.defaultdict(list)
        
        for idx, (k, trim) in enumerate(queries):
            lookup[trim].append((idx, k))
        
        def trim_nums(nums, trim):
            nnums = []
            for idx, num in enumerate(nums):
                nnums.append((num[-trim: ], idx))
            return nnums
        
        
        for trim, pairs in lookup.items():
            nnums = trim_nums(nums, trim)
            nnums.sort()
            for res_idx, k in pairs:
                res[res_idx] = nnums[k - 1][1]
        return res
            

        
