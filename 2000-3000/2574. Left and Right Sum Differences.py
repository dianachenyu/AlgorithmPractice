# Method 1: O(n), O(n)
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        ans = [0] * n
        for i in range(1, n):
            left[i] += left[i - 1] + nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] += right[i + 1] + nums[i + 1]
        for i in range(n):
            ans[i] = abs(left[i] - right[i])
        return ans 
      
      
# Method 2: O(n), O(n)
class Solution:  
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rsum = 0
        lsum = 0
        ans = [0] * n
        for i in range(n):
            rsum += nums[i]
        for i in range(n):
            rsum -= nums[i]
            ans[i] = abs(rsum - lsum)
            lsum += nums[i]
        return ans
