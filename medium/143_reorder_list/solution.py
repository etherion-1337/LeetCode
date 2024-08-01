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

class NeetSolution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        time complexity: O(n)
        space complexity: O(1)
        """
        # determine first and second segment of linked list
        # slow.next will be the beginning of 2nd segment
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd segment
        second = slow.next
        # split the linked list to 2 segment
        slow.next = None
        # previous nodes default
        prev = None
        # iterate the (potential) shorter segment
        while second:
            # before break the link, cache first
            tmp = second.next
            # now point to prev
            second.next = prev
            # move prev to curr (i.e. second)
            prev = second
            # move curr (i.e. second) to (original) next
            second = tmp

        # merge
        # original second will be None
        # but prev will be the last node of the original 2nd seg, now becomes the new head of the reversed linked list
        first, second = head, prev
        while second:
            # cache before breaking the next to point to new nodes
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2