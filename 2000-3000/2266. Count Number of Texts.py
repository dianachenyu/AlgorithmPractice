class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        pressedKeys = "#" + pressedKeys
        n = len(pressedKeys)
        dp = [0] * n
        dp[0] = 1
        MOD = 10 ** 9 + 7
        
        for i in range(1, n):
            dp[i] += dp[i - 1]
            
            for d in range(2, 5):
                if i - d >= 0 and pressedKeys[i - d + 1] == pressedKeys[i] and (d < 4 or pressedKeys[i] in '79'):
                    dp[i] += dp[i - d]
                else:
                    break
            dp[i] %= MOD   

        return dp[-1] 
            
        
