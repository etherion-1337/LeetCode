from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        use a hash set to store the visited nodes
        """
        hash_set = []
        curr = head

        while curr:
            if curr not in hash_set:
                hash_set.append(curr)
            else:
                return True
            curr = curr.next
            
        return False