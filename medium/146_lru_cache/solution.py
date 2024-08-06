class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        # doubly linked list
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # map key to node
        self.cache = {}
        # left = least recently used
        # right = most recently used
        self.left = Node(0,0)
        self.right = Node(0,0)
        # initially link these left and right first
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from anywhere in ll
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at the most right (but before self.right)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        # prev and self.right point to node
        prev.next = nxt.prev = node
        # node point to prev and self.right
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # update this node to most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove first and then insert to the right
            self.remove(self.cache[key])
        # new node, so inseat into cache hashmap first
        self.cache[key] = Node(key, value)
        # insert into the doubly ll
        self.insert(self.cache[key])

        # if exceeded capacity, evict LRU
        if len(self.cache) > self.cap:
            # LRU is the next of self.left
            lru = self.left.next
            # remove from ll
            self.remove(lru)
            # remove from cache hashmap
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)