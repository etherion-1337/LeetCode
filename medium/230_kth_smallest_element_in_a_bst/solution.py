from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    """
    DFS solution to get all the nodes in the tree and then sort them to get the kth smallest element
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.node_list = []

    def dfs(self, curr):
        if not curr:
            return 0
        
        left = self.dfs(curr.left)
        right = self.dfs(curr.right)

        self.node_list.append(curr.val)

        return 1+max(left, right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        height = self.dfs(root)
        res = sorted(self.node_list)[k-1]
        return res
    
class NeetSolution:
    """
    Iterative solution to get the kth smallest element in the BST
    Use a stack to keep track of the nodes
    In order traversal: left -> root -> right
    Since it is a BST, we add all the left nodes to the stack first
    When hit a leaf node, we went back and pop the stack
    This order will give us smallest to largest elements
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # counter for how many nodes we have visited
        n = 0
        # stack to keep track of the nodes
        stack = []
        # pointer to current node
        curr = root

        while curr or stack:
            # add all the most left nodes to the stack
            while curr:
                stack.append(curr)
                curr = curr.left
            # if reach here means we have visited all the left nodes and reaches the leaf
            # then we back track one level and pop the stack
            # if we have visited k nodes, then this is the kth smallest element
            # else we move to the right node and continue the process of visiting the left nodes first (in the next iteration)
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            else:
                curr = curr.right