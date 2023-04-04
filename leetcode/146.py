class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = self.right = None
    def pop(self):
        l, r = self.left, self.right
        if l:
            l.right = r
        if r:
            r.left = l
        self.left = self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.head = Node(None, None)
        self.tail = self.head
        self.cap = capacity

    def mark(self, node):
        if node == self.tail:
            self.tail = self.tail.left
        node.pop()
        self.tail.right = node
        node.left = self.tail    
        self.tail = node
        
    def get(self, key: int) -> int:
        if key in self.d:
            ret = self.d[key].val
            self.mark(self.d[key])
            return ret
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].val = value
        else:
            self.d[key] = Node(key, value)
        self.mark(self.d[key])
        
        if len(self.d) > self.cap:
            to_kill = self.head.right
            to_kill.pop()
            del self.d[to_kill.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)