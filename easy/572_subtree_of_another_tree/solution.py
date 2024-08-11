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
        # this covers the edge case where root is not None but subroot is None -> yes it is subtree
        # think of it the leaf node will lead to None child node which is the same as the (Null) subroot
        # this also covers the edge case where both root and subroot are None -> yes it is subtree
            return True
        elif not root or not subroot:
            return False
        elif root.val != subroot.val:
            return False

        left_check = self.isSameTree(root.left, subroot.left)
        right_check = self.isSameTree(root.right, subroot.right)

        return (left_check and right_check)
    
class NeetSolution:
    """
    time complexity: O(n * m) where n is the number of nodes in the main tree and m is the number of nodes in the subtree
    """
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:         # i think this first if statement is not necessary, this will be covered by the first if in the sameTree function, when it traverse to the end of the main tree
            return True
        # order matters, here is really "if not root and subRoot", but subRoot is checked in the first if statement
        # this if statement is necessary for isSubtree to backtrack when it reaches the end of main tree
        # it also covers the edge case where root is None but subRoot is not None -> no, not a subtree
        # although the this case is also covered in the (return) exit condition of the sameTree function
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        # this means that one of the root/subRoot is None and the other is not, hence not the same tree
        return False