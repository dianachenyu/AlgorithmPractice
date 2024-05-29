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


# Note: Prerequisite of this question is the contraint "p and q will exist in the tree."

# Similar Questions
# 235. Lowest Common Ancestor of a Binary Search Tree
# 236. Lowest Common Ancestor of a Binary Tree
# 1644. Lowest Common Ancestor of a Binary Tree II. remove the constraint that p and q exist in the tree
# 1650. Lowest Common Ancestor of a Binary Tree III. given parent of each node, not given tree root
# 1676. Lowest Common Ancestor of a Binary Tree IV. find LCA of k nodes
# 1123. Lowest Common Ancestor of Deepest Leaves

