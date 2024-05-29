# Question
# Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.

# Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -109 <= Node.val <= 109
# All Node.val are unique.
# All nodes[i] will exist in the tree.
# All nodes[i] are distinct.

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
# Output: 2
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
# Output: 1
# Example 3:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
# Output: 5


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
    
        def dfs(node):
            if not node:
                return None
            if node in nodes:
                return node
            
            lnode = dfs(node.left)
            rnode = dfs(node.right)
            if lnode and rnode:
                return node
            return lnode or rnode

        return dfs(root)


# Similar Questions
# 235. Lowest Common Ancestor of a Binary Search Tree
# 236. Lowest Common Ancestor of a Binary Tree
# 1644. Lowest Common Ancestor of a Binary Tree II. remove the constraint that p and q exist in the tree
# 1650. Lowest Common Ancestor of a Binary Tree III. given parent of each node, not given tree root
# 1676. Lowest Common Ancestor of a Binary Tree IV. find LCA of k nodes
# 1123. Lowest Common Ancestor of Deepest Leaves
