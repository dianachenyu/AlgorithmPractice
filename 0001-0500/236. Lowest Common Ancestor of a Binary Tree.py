# Method 1
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def dfs(node):
            nonlocal res
            if not node:
                return False, False
         
            pl, ql = dfs(node.left)
            pr, qr = dfs(node.right)
            find_p = pl or pr or (node == p)
            find_q = ql or qr or (node == q)
            if find_p and find_q and not res:
                res = node
            return find_p, find_q
        
        dfs(root)
        return res 

# Method 2
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            if node == p or node == q:
                return node
                
            l = dfs(node.left)
            r = dfs(node.right)
            if l and r:
                return node
            return l or r
        return dfs(root)


# Prerequisite of this question is the contraint "p and q will exist in the tree."
