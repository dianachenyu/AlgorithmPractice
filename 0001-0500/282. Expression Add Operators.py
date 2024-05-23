class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []
        def dfs(idx, path, value, last):
            if idx == n:
                if value == target:
                    res.append(path)
                return 

            for nidx in range(idx + 1, n + 1):
                if nidx > idx + 1 and num[idx] == '0':
                    return 
                cur = num[idx: nidx]
                cur_int = int(cur)
                if idx == 0:
                    dfs(nidx, cur, cur_int, cur_int)
                else:
                    dfs(nidx, path + '+' + cur, value + cur_int, cur_int)
                    dfs(nidx, path + '-' + cur, value - cur_int, -cur_int)
                    dfs(nidx, path + '*' + cur, value - last + last * cur_int, last * cur_int)
            
        dfs(0, "", 0, 0)
        return res 
