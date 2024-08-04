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
        time complexity: O(n)
        space complexity: O(n)
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
    
class NeetSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        space O(1) solution
        use two pointers, slow and fast
        fast to catch up slow, if there is a cycle, they will meet
        every iteration, the distance between slow and fast will decreased by 1 if there is a cycle
        therefore the time complexity is O(n)
        time complexity: O(n)
        space complexity: O(1)
        """
        slow, fast = head, head

        # fast need to jump twice, so need to make sure is not None 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False