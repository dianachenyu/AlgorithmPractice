class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        res = 0
        diff = (int(correct[0:2]) - int(current[0:2])) * 60 + int(correct[3:5]) - int(current[3:5])
        for num in [60, 15, 5, 1]:
            res += diff // num
            diff %= num
        return res
