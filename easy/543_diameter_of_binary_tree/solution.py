from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Use DFS to traverse the tree
    The (returned) height of the tree is not needed here directly but needed to calculate the diameter
    Rather we keep track a global variable: diameter = left + right
    time complexity: O(n)
    """
    def __init__(self):
        self.diameter = 0

    def dfs(self, curr):
        if not curr:
            return 0
        
        left = self.dfs(curr.left)
        right = self.dfs(curr.right)

        self.diameter = max(self.diameter, left + right)

        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        height = self.dfs(root)

        return self.diameter 