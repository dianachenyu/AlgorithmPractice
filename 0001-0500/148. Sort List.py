# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def split(node):
            slow = fast = node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            ltail, rhead = slow, slow.next
            ltail.next = None
            return rhead
                                 

        def merge(node):
            if not node or not node.next:
                return node
            
            rhead = split(node)
            lhead = merge(node)
            rhead = merge(rhead)
            dummy = ListNode(0)
            cur = dummy
            while lhead and rhead:
                if lhead.val <= rhead.val:
                    cur.next = lhead
                    lhead = lhead.next
                else:
                    cur.next = rhead
                    rhead = rhead.next
                cur = cur.next
            cur.next = lhead or rhead
            return dummy.next
                
        return merge(head)    
     
# Time O(nlogn)
# Space O(logn)
