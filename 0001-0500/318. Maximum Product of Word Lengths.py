# Method 1:
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        chars = []
        for word in words:
            chars.append(set(word))
        
        n = len(words)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if not chars[i] & chars[j]:
                    res = max(res, len(words[i]) * len(words[j]))
        return res

# Time O(mn + n * n), n = len(words), m = avg length of word
# Space O(n)


# Method 2:
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        res = 0
        bits = []
        for word in words:
            bit = 0
            for char in word:
                bit |= 1 << (ord(char) - ord('a'))
            bits.append(bit)
        
        for i in range(n):
            for j in range(i + 1, n):
                if not bits[i] & bits[j]:
                    res = max(res, len(words[i]) * len(words[j]))
        return res

# Time O(mn + n * n), n = len(words), m = avg length of word
# Space O(n)
       
