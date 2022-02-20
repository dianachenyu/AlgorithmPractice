# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        total = 0
        while head:
            if head.val == 0 and total > 0:
                tail.next = ListNode(total)
                total = 0
                tail = tail.next
            else:
                total += head.val
            head = head.next
        return dummy.next 
                
        
