class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)
        n = len(s)
        count = 0
        i = n - 1

        while i > 0: 
            while s[i] == '0' and i > 0:
                count += 1
                i += 1
            if i == 0:
                return count
            while s[i] == '1' and i > 0:
                count += 1
                i += 1
            count += 1
            if i == 0:
                return count + 1
            s[i] = '1'
        return count 
