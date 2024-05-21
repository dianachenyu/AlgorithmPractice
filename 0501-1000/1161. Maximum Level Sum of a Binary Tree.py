# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = 1
        level = 1
        max_sum = root.val
        stack = [root]

        while stack:
            nstack = []
            ssum = 0
            for node in stack:
                ssum += node.val
                if node.left:
                    nstack.append(node.left)
                if node.right:
                    nstack.append(node.right)
            if ssum > max_sum:
                res = level
                max_sum = ssum
            level += 1
            stack = nstack
        return res 
