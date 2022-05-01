class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        counti = countj = 0
        
        while i >= 0 or j >= 0:
            if i >= 0 and s[i] == '#':
                counti += 1
                i -= 1
            elif j >= 0 and t[j] == '#':
                countj += 1
                j -= 1
            elif i >= 0 and counti > 0:
                counti -= 1
                i -= 1    
            elif j >= 0 and countj > 0:
                countj -= 1
                j -= 1      
            elif i >= 0 and j >= 0: 
                if s[i] != t[j]:
                    return False
                else:
                    i -= 1
                    j -= 1
            else:
                break

        return i == -1 and j == -1
        
