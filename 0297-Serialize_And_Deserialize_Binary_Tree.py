# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
- bfs
- O(n), O(n)
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = [root]
        result = []
        node = root
        while q:
            node = q.pop(0)
            if not node:
                result.append("#")
            else:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        der = data.split(",")
        if der[0] == "#": return None
        root = TreeNode(int(der.pop(0)))
        q = [root]
        i = 0
        while q:
            node = q.pop(0)
            if der[i] != "#":
                node.left = TreeNode(int(der[i]))
                q.append(node.left)
            i += 1
            if der[i] != "#":
                node.right = TreeNode(int(der[i]))
                q.append(node.right)
            i += 1
        return root

"""
- dfs (preorder)
- O(n), O(n)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return " "
        return f"{str(root.val)}#{self.serialize(root.left)}#{self.serialize(root.right)}"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split("#") # convert to a list to make computation easier
        return self.derHelper(data_list)
    
    def derHelper(self, data_list):
        if data_list[0] == " ":
            data_list.pop(0)
            return None
        root = TreeNode(str(data_list[0]))
        data_list.pop(0)
        root.left = self.derHelper(data_list)
        root.right = self.derHelper(data_list)
        return root
        

# Your Codec object will be instantiated and called as such:
root = TreeNode(-1)
root.left = TreeNode(0)
root.right = TreeNode(1)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)

codec = Codec()
serialized = codec.serialize(root)
deserialized = codec.deserialize(serialized)
print(deserialized)