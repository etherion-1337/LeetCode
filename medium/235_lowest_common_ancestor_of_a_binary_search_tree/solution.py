# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    note that this is a binary search tree, so we can use the property of BST to solve this problem
    During recursion, as long as p and q are in different side of the root, the root is the lowest common ancestor
    time complexity: O(log n): we only need to traverse the height of the tree (i.e. one side of the tree), so usually it is log n
    space complexity: O(1)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        A few edge cases to consider:
        1) no need to check which is smaller or larger, since the question does not specify that p is smaller than q
        if both are smaller or bigger than current root, they go to the same side
        if one is smaller and one is bigger, it falls to the Else case no matter which is smaller or bigger
        2) if p or q is the current root, then the root is the lowest common ancestor, which also falls to the Else case.
        """
        while True: # result is guaranteed to be found
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
            

class NeetSolution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
            