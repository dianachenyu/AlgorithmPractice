from collections import Counter
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        s_counters = [Counter(sticker) for sticker in stickers]
        
        @cache
        def dp(target):
            if not target:
                return 0

            t_counter = Counter(target) 
            res = float('inf')
            for s_counter in s_counters:
                if target[0] in s_counter: # Working on the first char in target in the current round, must reduce its count
                    n_target = ''.join([char * count for char, count in (t_counter - s_counter).items()])
                    this_res = dp(n_target) + 1
                    res = min(res, this_res)
            return res 

        res = dp(target)
        return res if res < float('inf') else -1
