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
    
class NeetSolution:
    """
    Almost identical to the above solution, but with a different way of returning the height of the subtree.
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            # make sure not only the current node is balanced, but also the left and right subtree are balanced
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]