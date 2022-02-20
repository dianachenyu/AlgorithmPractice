class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = [-num * 2 if num % 2 else -num for num in nums]
        min_num = -max(heap)
        heapq.heapify(heap)
        res = float('inf')
        
        while len(heap) == len(nums):
            max_num = -heapq.heappop(heap)
            res = min(res, max_num - min_num)
            if max_num % 2 == 0:
                min_num = min(min_num, max_num // 2)
                heapq.heappush(heap, -max_num // 2)
        return res 
    
# Time O(nmlogn)
# Space O(n)
# n = len(nums), m = max(nums)
