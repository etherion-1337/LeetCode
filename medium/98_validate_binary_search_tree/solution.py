from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    DFS solution
    time complexity: O(n)
    children within tree will bounded by immeidate parent and the one above 
    children at the side of the tree is bounded by parent and +- inf.
    """
    def dfs(self, curr, left, right):
        # an empty bst is still a valid bst
        if not curr:
            return True
        if not (left < curr.val < right):
            return False

        left_check = self.dfs(curr.left, left, curr.val)
        right_check = self.dfs(curr.right, curr.val, right)

        return (left_check and right_check)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = self.dfs(root, float("-inf"), float("inf"))
        return result
    
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))