class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        cur = head
        while cur:
            nxt = cur.next
            cur.next = Node(cur.val)
            cur.next.next = nxt
            cur = nxt
     
        old_cur = head
        while old_cur:
            if old_cur.random:
                new_cur = old_cur.next
                new_cur.random = old_cur.random.next
            old_cur = old_cur.next.next

        old_cur = head
        new_head = head.next
        while old_cur:
            new_cur = old_cur.next
            old_cur.next = old_cur.next.next
            if new_cur.next:
                new_cur.next = new_cur.next.next
            old_cur = old_cur.next
        return new_head

  
  
# Time O(n), Space O(1)
