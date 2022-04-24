class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set()
        
        def get_points(x, y, r):
            points = []
            for x1 in range(x - r, x + r + 1):
                diff_y_sqr = r ** 2 - (x1 - x) ** 2
                y1 = math.ceil(y - math.sqrt(diff_y_sqr))
                y2 = math.floor(y + math.sqrt(diff_y_sqr))
                for y3 in range(y1, y2 + 1):
                    points.append((x1, y3))
            return points
        
        for x, y, r in circles:
            points= get_points(x, y, r)
            res |= set(points)
        return len(res)
