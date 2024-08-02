from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        tail = head
        count = 0
        # count the number of nodes
        while dummy:
            count += 1
            dummy = dummy.next

        # move the tail pointer to the node before the node to be removed
        remove_node = count - n
        for _ in range(remove_node-1):
            tail = tail.next

        # if the node to be removed is the head node
        # we start the new head from the next node
        if remove_node == 0:
            head = tail.next
        # normal cases
        elif tail.next and tail.next.next:
            tail.next = tail.next.next
        # if the node to be removed is the tail node
        # edge case: only node in the linked list
        elif tail.next is None:
            head = None
        # edge case: the node to be removed is the second last node
        elif tail.next.next is None:
            tail.next = None

        return head
    
class NeetSolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        # create a dummy node before head
        dummy = ListNode(0, head)
        # left and right pointer
        # the space between them is n + 1 
        # such that with r reaches the end, l is at the node to be broken
        l = dummy
        r = head
        # find out the starting point of r
        while n > 0 and r:
            r = r.next
            n -= 1
        # shift both l and r
        # when r reaches the end
        # l is at the right node
        while r:
            l = l.next
            r = r.next
        # reroute linked list (l) to drop the specific node
        l.next = l.next.next
        # ignore the first dummy node we added
        return dummy.next