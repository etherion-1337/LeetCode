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
    Similar to qn 102, but we need to return the rightmost node of each level   
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        bfs_result = []
        q = deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            bfs_result.append(level)
            
        result = [level[-1] for level in bfs_result]
        return result