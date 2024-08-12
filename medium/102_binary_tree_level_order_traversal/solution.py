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
    time complexity: O(n)
    space complexity: O(n/2) ~ O(n) (worst case when the tree is a complete binary tree)
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
            # at the last tier, q can be non-empty (i.e. [None, None, None, None] due to the last tier) but node is empty
            if _order:
                order.append(_order)
        return order
    
class NeetSolution:
    """
    Very similar to the above solution
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                # note the difference here
                # we first add node.val then check if node.left and node.right exist
                # hence there is no need to check if val is empty.
                # we are adding the node.val to the val list first
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res
    
class NeetSolution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Another variation of the above solution
        """
        result = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # at the last tier, q can be non-empty (i.e. [None, None, None, None] due to the last tier) but node is empty
            if level:
                result.append(level)

        return result