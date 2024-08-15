from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Use recursive approach to build the tree
    Use preorder and inorder properties to slice and compartmentalize the tree recursively
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # first node of preorder list is always going to be root
        # second node of preorder list is going to be the root of the left sub tree
        root = TreeNode(preorder[0])
        # the left part of root in inorder list are all nodes from left subtree
        mid = inorder.index(preorder[0])
        # first node is the root, so we exclude
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root