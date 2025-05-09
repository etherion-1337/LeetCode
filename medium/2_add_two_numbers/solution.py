from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        use python list to store the value of l1 and l2
        """
        # retrieve the value of l1 and l2
        l1_list = []
        l2_list = []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        # calculate the sum of l1 and l2
        l1_val = 0
        l2_val = 0
        for i, num in enumerate(l1_list):
            if i == 0:
                l1_val += num
            else:
                l1_val += num*(10**i)
        for i, num in enumerate(l2_list):
            if i == 0:
                l2_val += num
            else:
                l2_val += num*(10**i)
        ans = l1_val + l2_val
        # create the linked list
        # use str trick to break the number into digits
        l3_list = [int(val) for val in list(str(ans))]
        l3_list.reverse()
        for i, num in enumerate(l3_list):
            if i == 0:
                head = ListNode(num)
                tmp = head
            else:
                tmp.next = ListNode(num)
                tmp = tmp.next

        return head

class NeetSolution:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        # if carry is 1, then the next digit should be added 1
        carry = 0
        # carry is added to while condition is to handle the edge case when both list is none but carry is 1
        # so extra noded need to be added
        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            # new digit
            val = val_1 + val_2 + carry
            if val >= 10:
                carry = 1
                val = val % 10
            else:
                carry = 0

            curr.next = ListNode(val)
            # update the pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next        