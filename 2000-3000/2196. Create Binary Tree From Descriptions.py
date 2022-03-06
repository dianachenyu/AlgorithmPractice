class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        find_children = dict()
        for parent, child, isLeft in descriptions:
            if parent not in find_children:
                find_children[parent] = [-1, -1]
            if isLeft:
                find_children[parent][0] = child
            else:
                find_children[parent][1] = child
        
        root_set = set([parent for parent, _, _ in descriptions]) - set([child for _, child, _ in descriptions])
        root_val = root_set.pop()
        root = TreeNode(root_val)
        
        def dfs(node):
            if node and node.val in find_children:
                lval, rval = find_children[node.val]
                if lval > 0:
                    node.left = TreeNode(lval)
                    dfs(node.left)
                if rval > 0:
                    node.right = TreeNode(rval)
                    dfs(node.right)
        
        dfs(root)
        return root
            
