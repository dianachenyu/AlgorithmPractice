# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        i = 0
        j = 0
        
        while head:
            res[i][j] = head.val
            head = head.next
            
            di = directions[d][0]
            dj = directions[d][1]
            if not (0 <= i + di < m and 0 <= j + dj < n and res[i + di][j + dj] < 0):
                d = (d + 1) % 4
                di = directions[d][0]
                dj = directions[d][1]
            i += di
            j += dj
        return res 

        
