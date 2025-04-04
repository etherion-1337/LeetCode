from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """"
        same as question #1123 lowest_common_ancestor_of_deepest_leaves
        """
                
        def dfs(node, depth):
            if not node:
                return (None, depth + 1)
            
            left_node, left_depth = dfs(node.left, depth + 1)
            right_node, right_depth = dfs(node.right, depth + 1)

            if left_depth > right_depth:
                return left_node, left_depth
            elif left_depth < right_depth:
                return right_node, right_depth
            else:
                return node, left_depth

        node, _ = dfs(root, 0)

        return node