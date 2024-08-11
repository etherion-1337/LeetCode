from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    For each node in the main tree, check if the subtree is same as the subroot.
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the main tree is empty, or it reached the end of the main tree, return False
        if not root:
            return False
        # check if the current node (and its children) is the same as the subroot
        if self.isSameTree(root, subRoot):
            return True
        # check if the subtree is in the left or right of the main tree
        main_left_check = self.isSubtree(root.left, subRoot)
        main_right_check = self.isSubtree(root.right, subRoot)
        # either left or right branch return True then it will be true
        return (main_left_check or main_right_check)

    def isSameTree(self, root, subroot):
        """
        same as Qn 100: Same Tree
        """
        if not root and not subroot:
            return True
        elif not root or not subroot:
            return False
        elif root.val != subroot.val:
            return False

        left_check = self.isSameTree(root.left, subroot.left)
        right_check = self.isSameTree(root.right, subroot.right)

        return (left_check and right_check)