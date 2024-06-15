class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = [(-p, c) for c, p in zip(capital, profits) if c <= w]
        min_heap = [(c, -p) for c, p in zip(capital, profits) if c > w]
        heapq.heapify(max_heap)
        heapq.heapify(min_heap)
        while k and max_heap:
            p, c = heapq.heappop(max_heap)
            w += -p
            k -= 1
            while min_heap and min_heap[0][0] <= w:
                c, p = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (p, c))
        return w 

