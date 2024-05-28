# solution 1: filling vertically 
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        m = max(map(len, words))
        n = len(words)
        matrix = [[' ' for _ in range(n)] for _ in range(m)]
        for j, word in enumerate(words):
            for i, ch in enumerate(word):
                matrix[i][j] = ch
        ans = [''.join(word) for word in matrix]
        ans = [word.rstrip(' ') for word in ans]
        return ans
        
        
# solution 2         
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        ans = []
        m = max(map(len, words))
        for i in range(m):
            nword = ''.join(word[i:i+1] or ' ' for word in words)
            ans.append(nword.rstrip())
        return ans 
        
