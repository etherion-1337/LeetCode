from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    Since the all leaf node is specified as "N", this can be considered as a full binary tree.
    So we can only use the preorder traversal to serialize and deserialize the tree.
    If not we need use inorder too.
    """
    def preorder_dfs_ser(self, curr):
        if not curr:
            self.preorder_arr.append("N")
            return 

        self.preorder_arr.append(str(curr.val))
        self.preorder_dfs_ser(curr.left)
        self.preorder_dfs_ser(curr.right)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.preorder_arr = []
        self.preorder_dfs_ser(root)
    
        data = ",".join(self.preorder_arr)
        return data

    def preorder_dfs_deser(self, data_list):
        if data_list[self.pointer] == "N":
            self.pointer += 1
            return None
        
        node = TreeNode(int(data_list[self.pointer]))
        self.pointer += 1
        node.left = self.preorder_dfs_deser(data_list)
        node.right = self.preorder_dfs_deser(data_list)
        return node


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(",")
        self.pointer = 0

        root = self.preorder_dfs_deser(data_list)
        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

class NeetCodec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()