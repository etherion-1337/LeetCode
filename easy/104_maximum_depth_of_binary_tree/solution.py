from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DFSSolutionRecursive:
    """
    Recursive DFS solution
    time complexity: O(n)
    space complexity: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftmax = self.maxDepth(root.left)
        rightmax = self.maxDepth(root.right)

        return 1 + max(leftmax, rightmax)

class BFSSolution:
    """
    iterative BFS
    use a deque to store the nodes in the same level
    time complexity: O(n)
    space complexity: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        q = deque([root])

        while q:
            # take a snap shot at current q
            # replace all nodes with their children
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level
    
class DFSSolutionIterative:
    """
    Iterative DFS solution
    use a stack to store the nodes and their depth
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res