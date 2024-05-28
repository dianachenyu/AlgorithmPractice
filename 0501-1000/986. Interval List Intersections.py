class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        n1 = len(firstList)
        n2 = len(secondList)
        i = j = 0

        while i < n1 and j < n2:
            start = max(firstList[i][0], secondList[j][0])
            end =  min(firstList[i][1], secondList[j][1])
            if start <= end:
                res.append([start, end])
            if firstList[i][1] <= secondList[j][1]:
                    i += 1
            else:
                    j += 1
        return res
