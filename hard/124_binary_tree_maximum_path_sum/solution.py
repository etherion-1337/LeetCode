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
    for each node, we compute the max path sum with and without split
    the max path sum without split is returned to the parent node (since if path comes from parent node, we cannot split), because once we we split, our path cannot go back to parent node
    the max path sum with split is computed by adding the current node value and the max path sum without split of left and right child nodes, this value is used to update our potential result
    """
    def dfs(self, curr):
        if not curr:
            return 0

        left_max = self.dfs(curr.left)
        right_max = self.dfs(curr.right)
        left_max = max(left_max, 0)
        right_max = max(right_max, 0)

        # compute max path sum WITH split
        self.result = max(self.result, curr.val + left_max + right_max)

        # return max path sum WITHOUT split
        return curr.val + max(left_max, right_max)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        dummy_res = self.dfs(root)
        return self.result
    
class NeetSolution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]