# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        head = ListNode(0)
        tail = head
        heap = []
        for idx, node in enumerate(lists):
            if node:
                heap.append([node.val, idx])
        heapq.heapify(heap)

        while heap:
            _, idx = heapq.heappop(heap)
            tail.next = lists[idx]
            tail = tail.next 
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(heap, [lists[idx].val, idx])
            tail.next = None

        return head.next
      
    
# LinkedList, Heap, Divided & Conquer
# Time O(NlogK), N = total number of nodes in K linkedlist, K=len(lists)
# Space O(K)
