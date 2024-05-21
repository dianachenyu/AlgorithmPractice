# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1: BFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            nstack = []
            res.append(stack[0].val)
            for node in stack:
                if node.right:
                    nstack.append(node.right)
                if node.left:
                    nstack.append(node.left)
            stack = nstack
        return res 


# Method 2: DFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, level):
            if not node:
                return
            if len(res) < level:
                res.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 1)
        return res 
