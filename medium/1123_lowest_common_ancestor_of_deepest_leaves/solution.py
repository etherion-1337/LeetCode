from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        time: O(n)
        space: O(n)
        n = number of nodes in the tree

        same as question #865 smallest_subtree_with_all_deepest_nodes
        """
        
        # return (LCA, height)
        # height here is the dist from the leaf to the curr node
        def dfs(node):
            if not node:
                return (None, 0)
            
            left_node, left_height = dfs(node.left)
            right_node, right_height = dfs(node.right)

            if left_height > right_height:
                return left_node, left_height + 1 # left branch is deeper, so thats where the leaf is at
            elif left_height < right_height:
                return right_node, right_height + 1
            else:
                return node, left_height + 1 # both same height, so curr node is the LCA for cur left and right

        node, _ = dfs(root)

        return node
    
class Solution:
    """
    use depth instead of height
    same as the above solution
    """
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
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