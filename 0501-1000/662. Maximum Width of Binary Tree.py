class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [(root, 0)]
        
        while stack:
            min_num, max_num = float('inf'), 0
            nstack = []
            for i in range(len(stack)):
                node, num = stack[i]
                min_num = min(min_num, num)
                max_num = max(max_num, num)
                if node.left:
                    nstack.append((node.left, num * 2))
                if node.right:
                    nstack.append((node.right, num * 2 + 1))
            res = max(res, max_num - min_num + 1)
            stack = nstack
        return res 
                    
