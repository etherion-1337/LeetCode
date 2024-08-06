from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        use list to store all values from all linked lists
        flat and sort the list
        recreate linked list from sorted list
        """
        val_list = []

        for ll in lists:
            tmp = []
            while ll:
                tmp.append(ll.val)
                ll = ll.next
            val_list.append(tmp)
        
        val_list_flat = []
        for l in val_list:
            val_list_flat += l
        
        val_list_flat = sorted(val_list_flat)

        head = dummy = ListNode()

        for node_val in val_list_flat:
            dummy.next = ListNode(node_val)
            dummy = dummy.next
            
        return head.next