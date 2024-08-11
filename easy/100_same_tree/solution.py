from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    time complexity: O(p + q)
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both node is None, then they are the same
        if not p and not q:
            return True
        # if one of the node (but not both) is None, then they are not the same
        elif not p or not q:
            return False
        # if val is diff, immediately return False from the current recursive
        elif p.val != q.val:
            return False

        left_check = self.isSameTree(p.left, q.left)
        right_check = self.isSameTree(p.right, q.right)

        return (left_check and right_check)