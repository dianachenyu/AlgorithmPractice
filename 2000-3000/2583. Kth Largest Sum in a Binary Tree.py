# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        counter = collections.defaultdict(int)
        
        def dfs(root, level):
            if not root:
                return 
            
            counter[level] += root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 0)
        sums = list(counter.values())
        if len(sums) < k:
            return -1
        sums.sort(reverse=True)
        return sums[k - 1]
      
      
  # Time O(NlogN), Space O(N)
  # Tree Traversal 
