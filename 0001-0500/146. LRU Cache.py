class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None 


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            old_node = self.dict[key]
            self._remove(old_node)
        
        node = Node(key, value)
        self.dict[key] = node
        self._add(node)

        if len(self.dict) > self.capacity:
            del self.dict[self.head.next.key]
            self._remove(self.head.next)

    def _remove(self, node):
        '''Remove node from double linked list'''
        pnode = node.prev
        nnode = node.next
        pnode.next = nnode
        nnode.prev = pnode
        node.next = None
        node.prev = None
    
    def _add(self, node):
        '''Add a node before tail'''
        pnode = self.tail.prev
        pnode.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = pnode



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
