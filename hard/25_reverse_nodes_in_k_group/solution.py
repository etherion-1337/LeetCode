from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        use a list to store all values from the linked list
        """
        val_list = []
        dummy = head
        # go through the ll to get all val
        while dummy:
            val_list.append(dummy.val)
            dummy = dummy.next
        # use list comprehension to reverse every k elements
        val_list = [val_list[i:i+k][::-1] if len(val_list[i:i+k])>=k else val_list[i:i+k] for i in range(0,len(val_list),k)]
        flat_list = [x for xs in val_list for x in xs]
        # reconstruct the linked list
        head = dummy = ListNode()
        for node_val in flat_list:
            dummy.next = ListNode(node_val)
            dummy = dummy.next
        return head.next
    
class NeetSolution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        time complexity: O(n)
        space complexity: O(1)
        https://www.youtube.com/watch?v=1UOPsfP85V4
        """
        # dummy node before head
        dummy = ListNode(0, head)
        # the node before the group we would like to reverse
        groupPrev = dummy

        while True:
            kth = self.getkth(groupPrev, k)
            # when we reach the end of ll
            # not enough node to perform reverse
            if not kth:
                break
            # this node is right after the last node (i.e. kth) of the grp
            groupNext = kth.next
            
            # reverse the group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # reconnect the group with the rest of the ll    
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getkth(self, curr, k):
        """
        given a node, find the node k away, i.e. kth node
        if curr == groupPrev, return will be the last node of the group
        """
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr