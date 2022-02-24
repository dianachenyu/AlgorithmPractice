"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node', lookup = {}) -> 'Node':
        lookup = dict()
        
        def dfs(node):
            nonlocal lookup
            if not node:
                return None 

            cnode = Node(val = node.val)
            lookup[node.val] = cnode
            for nnode in node.neighbors:
                if nnode.val not in lookup:
                    cnnode = dfs(nnode)
                else:
                    cnnode = lookup[nnode.val]
                cnode.neighbors.append(cnnode)
            return cnode
        
        return dfs(node)
        
# Time O(E+V) = O(E) for connected graph
# Space O(E+V) for lookup, O(V) for recursion. Total O(E+V) = O(E)
