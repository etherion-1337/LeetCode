from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    BFS solution
    Very similar to qn 104, but we need to keep track of nodes instead of level
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        order = []
        order.append([root.val])

        q = deque([root])
        while q:
            _order = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    _order.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    _order.append(node.right.val)
            if _order:
                order.append(_order)
        return order