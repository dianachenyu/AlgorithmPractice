class Solution:
    def repeatLimitedString(self, s: str, limit: int) -> str:
        counter = collections.Counter(s)
        count = list(map(list, counter.items()))
        count.sort()
        n = len(s)
        res = [''] * n
        k = limit
        for i in range(n):
            if k > 0:
                res[i] = count[-1][0]
                k -= 1
                count[-1][1] -= 1
                if count[-1][1] == 0:
                    count.pop(-1)
                    k = limit
            elif len(count) > 1:
                res[i] = count[-2][0]
                k = limit
                count[-2][1] -= 1
                if count[-2][1] == 0:
                    count.pop(-2)
        return ''.join(res)
