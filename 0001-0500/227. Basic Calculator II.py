# Method 1: Stack
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        operator = '+'
        stack = []
        for idx, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if char in '+-*/' or idx == len(s) - 1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack[-1] = stack[-1] * num
                else:
                    stack[-1] = math.trunc(stack[-1] / num)
                num = 0
                operator = char  
        return sum(stack)

      
# Method 2: 
class Solution:
    def calculate(self, s: str) -> int:
        operator = '+'
        res = num = lnum = 0
        for idx, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if char in '+-*/' or idx == len(s) - 1:
                if operator == '+':
                    res += lnum
                    lnum = num
                elif operator == '-':
                    res += lnum
                    lnum = -num
                elif operator == '*':
                    lnum *= num
                else:
                    lnum = math.trunc(lnum / num)
                num = 0
                operator = char  
        return res + lnum
        
