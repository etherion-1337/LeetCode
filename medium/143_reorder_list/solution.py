from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        time complexity: O(n)
        space complexity: O(n)
        """
        # save all nodes in a list
        node_list = []
        while head:
            node_list.append(head)
            head = head.next

        # initialize dummy node and tail node
        # dummy will store the final link list
        # tail will be the last node of the final link list 
        dummy = tail = ListNode()

        # l and r are two pointers to iterate the node_list
        l = 0
        r = len(node_list) - 1
        # left and right are two flags to control the direction of the pointer
        left = True
        right = False

        while l <= r:
            if left == True:
                tail.next = node_list[l]
                l += 1
                left = False
                right = True
                # cut the link between the node and the next node to avoid cycle
                tail = tail.next
                tail.next = None
            else:
                tail.next = node_list[r]
                r -= 1
                left = True
                right = False
                # cut the link between the node and the next node to avoid cycle
                tail = tail.next
                tail.next = None
        # dummy.next is the final link list        
        head = dummy.next