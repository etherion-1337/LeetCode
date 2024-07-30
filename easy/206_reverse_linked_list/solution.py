from typing import Optional


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    iterative solution
    time complexity: O(n)
    space complexity: O(1)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    

class Solution:
    """
    recursive solution
    time complexity: O(n)
    space complexity: O(n)

    if the example linked list is [1, 2, 3, 4, 5]
    In the recursive call, the deepest layer returns head = ListNode{val: 5, next: None} or [5]
    From the next layer up of the recursive call, head is now ListNode{val: 4, next: ListNode{val: 5, next: None}} or [4, 5], and newHead = ListNode{val: 5, next: None} or [5], as it is returned from the deepest call. 
    The [5]s in both head and newHead are the SAME listnode.
    Now, head.next.next = head, so your head should be [4, 5, 4, 5, 4, 5, 4, 5... (its cyclical)], and newhead should be [5, 4, 5, 4, 5, 4...)] since the [5] and [4] list nodes are the same between head and newHead. 
    Then call head.next = null so head should be effectively truncated to [4], since head.next is the node after [4] to be removed.
    newHead is truncated to [5, 4], since anything after the first [4] is removed.
    From the next level up the recursion call, head is [3, 4] since the listNode [5] was removed from head. 
    head.next.next = head changes head to [3, 4, 3, 4, 3...]. And newHead is [5, 4, 3, 4, 3, 4, 3...]. 
    Then head.next = null truncates head to [3]. Repeat until the list is reversed. 
    Head.next = null effectively stops the linkedList from referencing itself forever.
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
    

if __name__ == '__main__':
    # test case
    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    l1 = ListNode(1,ListNode(2, ListNode(3, None)))
    s = Solution()
    print(s.reverseList(l1))  # expect 5 -> 4 -> 3 -> 2 -> 1 -> None