# Time O(n) 
# Space O(1)

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while cur: # move down, diff level 
            dummy = Node(0)
            lnode = dummy
            while cur: # move right, same level
                if cur.left:
                    lnode.next = cur.left
                    lnode = lnode.next
                if cur.right:
                    lnode.next = cur.right
                    lnode = lnode.next
                cur = cur.next 
            cur = dummy.next        
        return root


