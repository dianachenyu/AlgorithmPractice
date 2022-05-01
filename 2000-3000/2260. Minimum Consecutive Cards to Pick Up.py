class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        index = dict()
        res = float('inf')
        for idx, card in enumerate(cards):
            if card in index:
                res = min(res, idx - index[card] + 1)
            index[card] = idx
        return res if res < float('inf') else -1
                
