# Question
# Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.
# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5

# Example 3:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
# Output: null


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def dfs(node):
            nonlocal res
            if not node or res:
                return False, False
            pl, ql = dfs(node.left)
            pr, qr = dfs(node.right)
            find_p = pl or pr or node == p
            find_q = ql or qr or node == q
            if find_p and find_q and not res:
                res = node
            return find_p, find_q

        dfs(root)
        return res


# Similar Questions
# 235. Lowest Common Ancestor of a Binary Search Tree
# 236. Lowest Common Ancestor of a Binary Tree
# 1644. Lowest Common Ancestor of a Binary Tree II. remove the constraint that p and q exist in the tree
# 1650. Lowest Common Ancestor of a Binary Tree III. given parent of each node, not given tree root
# 1676. Lowest Common Ancestor of a Binary Tree IV. find LCA of k nodes
# 1123. Lowest Common Ancestor of Deepest Leaves
