116. Populating Next Right Pointers in Each Node

# Method 1: BFS
# level by level 
# Time O(n) Space O(1)

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while head:
            cur = head
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next 
            head = head.left 
        return root 


# Method 2: DFS
#Time O(n) Space O(logn)

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(node):
            if not node:
                return 
            if node.left:
                node.left.next = node.right
            if node.right and node.next:
                node.right.next = node.next.left
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root
