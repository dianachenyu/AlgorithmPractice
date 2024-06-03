"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def recursion(node):
            head = tail = node
            if node.left:
                lh, lt = recursion(node.left)
                lt.right = node
                node.left = lt
                head = lh
            if node.right:
                rh, rt = recursion(node.right)
                rh.left = node
                node.right = rh
                tail = rt
            return head, tail
        
        if not root:
            return 
        head, tail = recursion(root)
        tail.right = head
        head.left = tail
        return head

