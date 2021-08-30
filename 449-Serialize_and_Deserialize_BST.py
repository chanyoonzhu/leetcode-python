# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
How is this different from Problem 297? 
There is no need to use "#" or "null" in BST which makes it more compact!
The reason is that we can reconstruct BST by only using preorder(/postorder/levelorder) traversal.
However, in the binary tree situation, we need to use preorder(/postorder/levelorder) + inorder to reconstruct the tree. If we want to directly construct BT, we have to use "#" or "null".
"""
"""
- dfs (preorder)
"""
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        stack, result = [], []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                result.append(str(node.val))
                node = node.left
            else:
                node = stack.pop().right
        return ','.join(result)
                
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        
        def helper(ser, bound = float("inf")):
            if not ser: return None
            if ser[0] == "" or int(ser[0]) > bound: return None # ser[0] == "" handles test case: [], where ser is [""]
            node = TreeNode(int(ser.pop(0)))
            node.left = helper(ser, node.val)
            node.right = helper(ser, bound)
            return node
             
        ser = data.split(",")
        return helper(ser)

"""
- todo: encode integer to bytes
"""

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans