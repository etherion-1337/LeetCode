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
    
