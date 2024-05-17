# Method 1:
# Time O(N)
# Space O(N)

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None 

        values = []
        while head:
            values.append(head.val)
            head = head.next

        def helper(start, end):
            if start > end:
                return None
            if start == end:
                return TreeNode(values[start])
            
            mid = (start + end)// 2
            nhead = TreeNode(values[mid])
            nhead.left = helper(start, mid - 1)
            nhead.right = helper(mid + 1, end)
            return nhead
        
        return helper(0, len(values) - 1)


# Method 2: directly work on LinkedList
# Time O(NlogN)
# Space O(N)

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def find_middle(node):
            slow = fast = node
            while fast and fast.next and fast.next.next and fast.next.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        if not head:
            return None 
        if not head.next:
            return TreeNode(head.val)
        
        lt = find_middle(head)
        nhead = lt.next
        lt.next = None
        tree_head = TreeNode(nhead.val)
        tree_head.left = self.sortedListToBST(head)
        tree_head.right = self.sortedListToBST(nhead.next)
        return tree_head
