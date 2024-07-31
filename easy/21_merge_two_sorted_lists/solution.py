from typing import Optional 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        time complexity: O(n)
        space complexity: O(1)

        use a dummy to start the linked list to avoid empty node edge case
        since tail and dummy are pointing to the same node (initially), we can use tail to traverse the linked list
        tail will be always pointing to the last node of the linked list
        while dummy keep track the whole linked list
        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next


        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
    
class SolutionRecursive:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        time complexity: O(n)
        space complexity: O(n)

        recursive approach
        """
        if not list1:
            return list2
        if not list2:
            return list1
        lil, big = (list1, list2) if list1.val < list2.val else (list2, list1)
        lil.next = self.mergeTwoLists(lil.next, big)
        return lil