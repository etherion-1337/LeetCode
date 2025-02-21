from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.node_val = set()
        if root:
            root.val = 0
            self.node_val.add(0)
            self._recover_bin_tree(root.left, 1)
            self._recover_bin_tree(root.right, 2)

    def _recover_bin_tree(self, cur_node, cur_val):
        if not cur_node:
            return
        
        cur_node.val = cur_val
        self.node_val.add(cur_val)
        self._recover_bin_tree(cur_node.left, 2 * cur_val + 1)
        self._recover_bin_tree(cur_node.right, 2 * cur_val + 2)

    def find(self, target: int) -> bool:
        return target in self.node_val
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)