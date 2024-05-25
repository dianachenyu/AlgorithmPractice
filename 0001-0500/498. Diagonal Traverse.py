class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        lines = collections.defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                lines[i + j].append(mat[i][j])

        for key in range(max(lines.keys()) + 1):
            if key % 2 == 0:
                lines[key].reverse()
            res.extend(lines[key])
        return res 

