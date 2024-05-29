# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)

        while root:
            if root.val > max_val:
                root = root.left
            elif root.val < min_val:
                root = root.right
            else:
                return root
        return None 

      
# Time O(H), H=height of binary search tree
# Space O(1)

# Similar Questions
# 235. Lowest Common Ancestor of a Binary Search Tree
# 236. Lowest Common Ancestor of a Binary Tree
# 1644. Lowest Common Ancestor of a Binary Tree II. remove the constraint that p and q exist in the tree
# 1650. Lowest Common Ancestor of a Binary Tree III. given parent of each node, not given tree root
# 1676. Lowest Common Ancestor of a Binary Tree IV. find LCA of k nodes
# 1123. Lowest Common Ancestor of Deepest Leaves

