from typing import Optional
import copy
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class CheeseSolution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_copy = copy.deepcopy(head)
        return new_copy
    
class Solution:
    """
    Two pass solution
    time: O(n)
    space: O(n)
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # hash map to store mapping from old node to new node (val only)
        # None is for the edge case where the random is point to None
        old2new_map = {None:None}

        # go through the list to copy val only
        curr = head
        while curr:
            old2new_map[curr] = Node(curr.val)
            curr = curr.next

        # go through the list again to link
        curr = head
        while curr:
            copy = old2new_map[curr]
            # now fill next and random
            copy.next = old2new_map[curr.next]
            copy.random = old2new_map[curr.random]
            curr = curr.next

        return old2new_map[head]