# Question
# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be from left to right.

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Example 2:
# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]
# Example 3:
# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        d = collections.defaultdict(list)
        queue = [[root, 0]]
        while queue:
            nqueue = []
            for node, col in queue:
                d[col].append(node.val)
                if node.left:
                    nqueue.append([node.left, col - 1])
                if node.right:
                    nqueue.append([node.right, col + 1])
            queue = nqueue
        
        res = []
        for col in range(min(d.keys()), max(d.keys())+ 1):
            res.append(d[col])
        return res 

