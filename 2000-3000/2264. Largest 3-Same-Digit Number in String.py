# Method 1
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for char in "9876543210":
            string = char * 3 
            if string in num:
                return string
        return ""

      
# Method 2
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        candidates = []
        for i in range(len(num) - 2):
            sub = num[i : i + 3]
            if sub[0] == sub[1] == sub[2]:
                candidates.append(sub)
        return max(candidates) if candidates else ""     

