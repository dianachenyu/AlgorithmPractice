class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int: 
        def getMaxIndex(points, skip=-1):
            max_sum, max_diff, min_sum, min_diff = -float('inf'), -float('inf'), float('inf'), float('inf')
            for idx, (x, y) in enumerate(points):
                if idx == skip:
                    continue
                if x + y > max_sum:
                    max_sum_index = idx
                    max_sum = x + y
                if x - y > max_diff:
                    max_diff_index = idx
                    max_diff = x - y
                if x + y < min_sum:
                    min_sum_index = idx
                    min_sum = x + y
                if x - y < min_diff:
                    min_diff_index = idx
                    min_diff = x - y
                
            if max_sum - min_sum >= max_diff - min_diff:
                return max_sum_index, min_sum_index
            else:
                return max_diff_index, min_diff_index

        def calculateDistance(points, idx1, idx2):
            return abs(points[idx1][0] - points[idx2][0]) + abs(points[idx1][1] - points[idx2][1])
        
        overall_x, overall_y = getMaxIndex(points)
        x1, y1 = getMaxIndex(points, overall_x)
        x2, y2 = getMaxIndex(points, overall_y)

        return min(calculateDistance(points, x1, y1), calculateDistance(points, x2, y2))

      
# Time O(N)
# Space O(1)
# classic problem to find the maximum Manhattan distance in O(n).
# https://stackoverflow.com/questions/8006697/finding-maximum-distance-between-x-y-coordinates
