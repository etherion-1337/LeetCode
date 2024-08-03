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