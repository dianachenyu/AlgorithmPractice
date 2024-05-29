# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return 0, None
            
            lh, lnode = dfs(node.left)
            rh, rnode = dfs(node.right)

            if lh > rh:
                return lh + 1, lnode
            if lh < rh:
                return rh + 1, rnode
            return lh + 1, node
        return dfs(root)[1]



# Similar Questions
# 235. Lowest Common Ancestor of a Binary Search Tree
# 236. Lowest Common Ancestor of a Binary Tree
# 1644. Lowest Common Ancestor of a Binary Tree II. remove the constraint that p and q exist in the tree
# 1650. Lowest Common Ancestor of a Binary Tree III. given parent of each node, not given tree root
# 1676. Lowest Common Ancestor of a Binary Tree IV. find LCA of k nodes
# 1123. Lowest Common Ancestor of Deepest Leaves
