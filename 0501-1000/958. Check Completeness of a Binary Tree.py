# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        find_null = False
        queue = [root]
        while queue:
            nqueue = []
            for node in queue:
                for nnode in [node.left, node.right]:
                    if nnode:
                        if find_null:
                            return False
                        nqueue.append(nnode)
                    else:
                        find_null = True
            queue = nqueue
        return True

