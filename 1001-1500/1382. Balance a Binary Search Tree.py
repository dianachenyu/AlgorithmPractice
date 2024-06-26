# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)
        
        def build_bst(left, right):
            if left > right:
                return 
            mid = (left + right) // 2
            node = nodes[mid]
            node.left = build_bst(left, mid - 1)
            node.right = build_bst(mid + 1, right)
            return node
