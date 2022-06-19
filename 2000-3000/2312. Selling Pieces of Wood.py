class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        lookup = collections.defaultdict(int)
        for h, w, price in prices:
            lookup[(h, w)] = price
        
        @functools.cache
        def dp(h, w):
            price = lookup[(h, w)]
            for h1 in range(1, h // 2 + 1):
                cur_price = dp(h1, w) + dp(h - h1, w)
                price = max(price, cur_price)
            for w1 in range(1, w // 2 + 1):
                cur_price = dp(h, w1) + dp(h, w - w1)
                price = max(price, cur_price)
            return price
        
        return dp(m, n)
