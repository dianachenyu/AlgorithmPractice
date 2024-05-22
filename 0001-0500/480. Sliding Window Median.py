class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return nums

        n = len(nums)
        res = []
        max_heap = [] # smaller half, bigger
        min_heap = [] # larger half
        to_remove = collections.defaultdict(int)

        def find_median(max_heap, min_heap, k):
            if k % 2:
                return -max_heap[0]
            else:
                return (-max_heap[0]+ min_heap[0])/2

        for idx, num in enumerate(nums[: k]):
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
        median = find_median(max_heap, min_heap, k)
        res.append(median)

        for idx in range(k, n):
            num = nums[idx]
            lnum = nums[idx - k]
            to_remove[lnum] += 1

            if lnum <= median:
                balance = -1
            else:
                balance = 1
            if num <= median:
                balance += 1
                heapq.heappush(max_heap, -num)
            else:
                balance -= 1
                heapq.heappush(min_heap, num)

            if balance < 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            elif balance > 0:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            while max_heap and to_remove[-max_heap[0]] > 0:
                to_remove[-max_heap[0]] -= 1
                heapq.heappop(max_heap)
            while min_heap and to_remove[min_heap[0]] > 0:
                to_remove[min_heap[0]] -= 1
                heapq.heappop(min_heap)
            median = find_median(max_heap, min_heap, k)
            res.append(median)
        return res 

      
# Time O(NlogN)
# Space O(N)
