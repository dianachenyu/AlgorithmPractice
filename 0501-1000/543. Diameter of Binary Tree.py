# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            n_left = dfs(node.left) 
            n_right = dfs(node.right) 
            res = max(res, n_left + n_right)
            return max(n_left, n_right) + 1
        
        dfs(root)
        return res
      
