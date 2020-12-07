# Time O(n)
# Space O(h)

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode: 
        dummy = TreeNode(0)
        nroot = dummy
        
        def dfs(root):
            nonlocal nroot
            if not root:
                return
            dfs(root.left)
            nnode = root.right
            root.left, root.right = None, None 
            nroot.right = root
            nroot = nroot.right      
            dfs(nnode)
        
        dfs(root)
        return dummy.right
