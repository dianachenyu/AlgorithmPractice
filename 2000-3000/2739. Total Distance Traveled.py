class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        return (min((mainTank - 1) // 4, additionalTank)  + mainTank) * 10

      
# Notes: https://leetcode.com/problems/total-distance-traveled/solutions/3650469/java-c-python-math-o-1/
# x <= additionalTank
# mainTank + x > 5x
