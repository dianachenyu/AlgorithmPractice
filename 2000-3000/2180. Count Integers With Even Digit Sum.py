class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for nnum in range(2, num + 1):
            ssum = 0
            for char in str(nnum):
                ssum += int(char)
            if ssum % 2 == 0:
                count += 1
        return count
        
