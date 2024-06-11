class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewards = sorted(set(rewardValues))
        # use ith bit to represent integer i in the bitset. 
        # at the begining, totals = {0}. set the first bit of binary to indicate x is 0.
        totals = 1
        for reward in rewards:
            # filtering out totals which total < reward
            valid_totals = totals & ((1 << reward) - 1)
            # for each value in valid_totals, we add reward to it
            # for example, if we have total = 5 (binary 100000) and reward = 6
            # then we will have new total = 11, whose binary = 10000000000 == (100000) << 6
            totals |= valid_totals << reward
        return totals.bit_length() - 1


# Time O(NlogN + MN/64), N=len(rewardValues), M=max(rewardValues)
# 64 is because Python deal with the bit operations in group of 64, or 32 depends on the machine.

# Great explanations
# https://leetcode.com/problems/maximum-total-reward-using-operations-ii/solutions/5282370/bitset-trick-include-similar-question/

