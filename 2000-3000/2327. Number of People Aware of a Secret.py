class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        new = [0] * (n + 1)
        new[1] = 1
        share = 0
        MOD = 10 ** 9 + 7
        
        for day in range(2, n + 1):
            if day - delay > 0:
                share += new[day - delay]
            if day - forget > 0:
                share -= new[day - forget]
            new[day] = share

        return sum(new[-forget:]) % MOD 
            
        
