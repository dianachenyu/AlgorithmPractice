# Method 1:
# Time O(n) Space O(1)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res[0] = abs(num)
            else:
                nums[abs(num) - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                res[1] = i + 1
        return res 

      
      
# Method 2: math
# Time O(n) Space O(1) 
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        x_minus_y = sum(nums) - n*(n+1)//2
        x2_minus_y2 = sum(x*x for x in nums) - n*(n+1)*(2*n+1)//6
        x_plus_y = x2_minus_y2//x_minus_y
        x, y = (x_plus_y + x_minus_y)//2, (x_plus_y - x_minus_y)//2
        return [x, y]
