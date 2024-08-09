from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    DFS solution.
    keep track of the height of the left and right subtree of each node.
    check if the difference between the height of the left and right subtree is greater than 1, for all nodes.
    This works because DFS return will give the height of the subtree rooted at the current node.
    time complexity: O(n)
    """
    def __init__(self):
        self.balanced = True

    def dfs(self, curr):
        if not curr:
            return 0
        
        left = self.dfs(curr.left)
        right = self.dfs(curr.right)

        if abs(left - right) > 1:
            self.balanced = False

        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        height = self.dfs(root)
        
        return self.balanced