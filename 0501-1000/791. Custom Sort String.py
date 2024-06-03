class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = collections.Counter(s)
        res = []
        for char in order:
            res.append(char * counter[char])
            counter[char] = 0
        for char in counter:
            res.append(char * counter[char])
        return ''.join(res)
