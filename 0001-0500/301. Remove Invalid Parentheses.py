from functools import cache 
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        count = delete = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                if count == 0:
                    delete += 1
                else:
                    count -= 1
        delete += count

        def dfs(idx, count, delete):
            res = set()
            if delete < 0 or count < 0:
                return res
            if idx == n:
                if count == 0:
                    res.add('')
                return res
            
            # Option 1: discard 
            if s[idx] == '(' or s[idx] == ')':
                res.update(dfs(idx + 1, count, delete - 1))
            
            # Option 2: keep
            if s[idx] == '(':
                count += 1
            if s[idx] == ')':
                count -= 1
            for suffix in dfs(idx + 1, count, delete):
                res.add(s[idx] + suffix)
            return res
        
        return dfs(0, 0, delete)
