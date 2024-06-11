class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewards = sorted(set(rewardValues))
        totals = {0}
        for reward in rewards:
            ntotals = set()
            for total in totals:
                if reward > total:
                    ntotals.add(reward + total)
            totals |= ntotals
        return max(totals)

      
# Key obersvation
# If rewardValues[i] is greater than your current total reward x, then add rewardValues[i] to x (i.e., x = x + rewardValues[i])
# 1 <= rewardValues[i] <= 2000
# So 1 <= total reward < 4000

# Time O(NlogN + MN), N=len(rewardValues), M=max(rewardValues)
