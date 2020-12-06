# Time O(n) 
# Space O(1)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, flower in enumerate(flowerbed):
            if not flower and (i == 0 or not flowerbed[i-1]) and (i == len(flowerbed)-1 or not flowerbed[i+1]):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False 
