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

