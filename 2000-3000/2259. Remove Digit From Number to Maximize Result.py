class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        removed = False
        res = []
        lidx = -1
        for idx in range(len(number)):
            if number[idx] != digit or removed:
                res.append(number[idx])
            elif (idx == len(number) - 1 or number[idx + 1] > digit):
                removed = True
            else:
                lidx = idx
                res.append(number[idx])
        if not removed:
            res[lidx] = ''
        return ''.join(res)
                
        
