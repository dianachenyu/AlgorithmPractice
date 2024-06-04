class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for idx, (x, y) in enumerate(points):
            heapq.heappush(heap, (-(x * x + y * y), idx))
            if len(heap) > k:
                heapq.heappop(heap)
        idxs = [idx for _, idx in heap]
        return [points[idx] for idx in idxs]



# Time O(NlogK), N=len(points)
# Space O(N+K)
