# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node):
            if not node:
                return 0, 0 
            
            nonlocal res 
            lsum, lcount = dfs(node.left)
            rsum, rcount = dfs(node.right)
            ssum = lsum + rsum + node.val
            count = lcount + rcount + 1
            res += ssum // count == node.val
            return ssum, count
            
        dfs(root)
        return res
