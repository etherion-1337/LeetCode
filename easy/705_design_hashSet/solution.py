class ListNode():
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    """
    Linked list implementation of hashset
    """
    def __init__(self):
        #10^4 dummy nodes, 10^4 cos this is expected num of calls of insertion
        self.set = [ListNode(0) for i in range(10**4)]
        
    def add(self, key: int) -> None:
        idx = key % len(self.set)
        curr = self.set[idx]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        idx = key % len(self.set)
        curr = self.set[idx]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        idx = key % len(self.set)
        curr = self.set[idx]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)