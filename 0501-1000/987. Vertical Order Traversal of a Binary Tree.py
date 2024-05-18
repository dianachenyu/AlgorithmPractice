# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = collections.defaultdict(list)
        queue = [[root, 0]]
        while queue:
            nqueue = []
            nd = collections.defaultdict(list)
            for node, col in queue:
                nd[col].append(node.val)
                if node.left:
                    nqueue.append([node.left, col - 1])
                if node.right:
                    nqueue.append([node.right, col + 1])
            queue = nqueue
            for col, values in nd.items():
                d[col].extend(sorted(values))
        res = []
        for col in range(min(d.keys()), max(d.keys()) + 1):
            res.append(d[col])
        return res 
