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
    

class NeetSolution:
    """
    merge every 2 linked lists until there is only 1 linked list
    an extension of merge 2 linked lists
    time complexity: O(nlogk)
    space complexity: O(1)
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            tmpLists = []
            # merge every 2 linked lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # l2 potentially can go out of bound
                # it is ok to merge 1 ll with a NULL ll
                l2 = lists[i+1] if (i+1) < len(lists) else None
                tmpLists.append(self.merge2Lists(l1, l2))
            lists = tmpLists
        return lists[0]

    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next