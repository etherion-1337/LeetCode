# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    time complexity: O(n)
    space complexity: O(h), where h is the height of the tree
    
    We use DFS, and track the maximum value (so far) from root to current node.
    If the current node value is greater than or equal to the maximum value, then it is a good node.
    """
    def dfs(self, curr, max_val):
        # empty tree has no good node
        if not curr:
            return 0 
        # for base case, we have 1 + left + right
        # 1 is for the current node (which is the root of subtree)
        # then add left and right good nodes number
        counter = 1 if curr.val >= max_val else 0 
        max_val = max(max_val, curr.val)
        left_good = self.dfs(curr.left, max_val)
        counter += left_good
        right_good = self.dfs(curr.right, max_val)
        counter += right_good

        return counter

    def goodNodes(self, root: TreeNode) -> int:
        # use negative value as placeholder to start
        # since constraints: node val within [1, 10^5]
        result = self.dfs(root, root.val)

        return result
    
class NeetSolution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)