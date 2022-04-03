class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = collections.defaultdict(int)
        for winner, loser in matches:
            loss[loser] += 1
            loss[winner] = loss[winner]
        ans = [[], []]
        for player, count in loss.items():
            if count == 0:
                ans[0].append(player)
            elif count == 1:
                ans[1].append(player)
        ans[0].sort()
        ans[1].sort()
        return ans
        
