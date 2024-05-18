# Method 1 
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        s = self.countAndSay(n - 1)
        res = []
        lchar = s[0]
        count = 1

        for char in s[1:]:
            if char == lchar:
                count += 1
            else:
                res.append(str(count) + lchar)
                lchar = char
                count = 1

        res.append(str(count) + lchar)
        return ''.join(res)


# Method 2
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(2, n + 1):
            res = []
            lchar = s[0]
            count = 1

            for char in s[1:]:
                if char == lchar:
                    count += 1
                else:
                    res.append(str(count) + lchar)
                    lchar = char
                    count = 1

            res.append(str(count) + lchar)
            s =''.join(res)
        return s
