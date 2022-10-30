# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # find depth and height of each node
        depths = collections.defaultdict(int)
        heights = collections.defaultdict(int)
        # cousins are node with the same depth
        cousins = collections.defaultdict(list)
        res = [0] * len(queries)
        
        def dfs(node, depth):
            if not node:
                return -1
            
            depths[node.val] = depth
            lheight = dfs(node.left, depth + 1)
            rheight = dfs(node.right, depth + 1)
            height = max(lheight, rheight) + 1
            heights[node.val] = height
            cousins[depth].append([height, node.val])
            return height
            
        dfs(root, 0) 
       
        # for each depth, keep top 2 node with largest height
        for depth in cousins:
            cousins[depth].sort(reverse=True)
            if len(cousins[depth]) > 2:
                cousins[depth] = cousins[depth][: 2]
        
        for idx, q in enumerate(queries):
            depth = depths[q]
            # if no other cousin 
            if len(cousins[depth]) == 1:
                res[idx] = depth - 1
            elif q == cousins[depth][0][1]:
                res[idx] = depth + cousins[depth][1][0]
            else:
                res[idx] = depth + cousins[depth][0][0]
        return res 
                
       
