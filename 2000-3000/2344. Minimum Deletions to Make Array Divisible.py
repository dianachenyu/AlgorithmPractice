class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        max_divisor = math.gcd(*numsDivide)
        count = 0
        heapq.heapify(nums)
        while nums:
            num = heapq.heappop(nums)
            if max_divisor % num == 0:
                return count
            if num > max_divisor:
                return -1
            count += 1
        return count 
        
