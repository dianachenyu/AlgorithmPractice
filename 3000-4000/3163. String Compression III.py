class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        lchar = word[0]
        count = 1
        for char in word[1:]:
            if char != lchar or count == 9:
                res.append(str(count) + lchar)
                lchar = char
                count = 1
            else:
                count += 1
        res.append(str(count) + lchar)
        return ''.join(res)

