class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        ans = [0] * n
        num = 0
        
        for i in range(n):
            num = num * 10 + int(word[i])
            num = num % m
            if num == 0:
                ans[i] = 1
        return ans
 
# Time O(n), Space O(n)
