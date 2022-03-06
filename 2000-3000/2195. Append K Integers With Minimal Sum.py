# Method 1
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.extend([0, 10 ** 9 + len(nums) + 1])
        nums.sort()
        n = len(nums)
        res = 0

        for i in range(n - 1):
            start = nums[i] + 1
            end = min(nums[i + 1] - 1, start + k - 1)
            count = end - start + 1
            if count <= 0:
                continue
            res += (start + end) * count //2
            k -= count
            
            if k == 0:
                return res

              
# Method 2
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        res = k * (k + 1) // 2
        last = k + 1
        nums = list(set(nums))
        nums.sort()
        
        for num in nums:
            if num < last:
                res += -num + last
                last += 1
        return res 
