class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':        
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        cur = head
        while cur.next != head:
            if cur.val <= insertVal <= cur.next.val:
                break
            
            if cur.val > cur.next.val and (cur.val <= insertVal or insertVal <= cur.next.val):
                break
            cur = cur.next
        
        nnode = Node(insertVal, cur.next)
        cur.next = nnode
        return head

  
