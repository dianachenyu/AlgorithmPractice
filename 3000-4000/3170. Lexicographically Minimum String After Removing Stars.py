class Solution:
    def clearStars(self, s: str) -> str:
        indexes = collections.defaultdict(list)
        s = list(s)
        for idx, char in enumerate(s):
            if char == '*':
                for lchar in string.ascii_lowercase:
                    if len(indexes[lchar]) > 0:
                        lidx = indexes[lchar].pop()
                        s[lidx] = ''
                        break
                s[idx] = ''
            else:
                indexes[char].append(idx)
        return ''.join(s)         
