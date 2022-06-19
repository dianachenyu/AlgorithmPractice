class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        for count in range(1, 11):
            if (k * count) % 10 == num % 10 and k * count <= num:
                return count
        return -1 
