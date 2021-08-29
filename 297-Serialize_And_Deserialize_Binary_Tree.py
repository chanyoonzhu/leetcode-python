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
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        # recursive
        self.preorder(root, result)
        # iterative
        """
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                result.append(str(node.val))
                node = node.left
            else:
                result.append("#")
                node = stack.pop().right
        """
        return ','.join(result)
    
    def preorder(self, node, ser):
        if not node:
            ser.append("#")
        else:
            ser.append(str(node.val)) # remember to str()
            self.preorder(node.left, ser)
            self.preorder(node.right, ser) 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        der = data.split(",")
        return self.dfs(der)
    
    def dfs(self, der):
        if not der: return None
        val = der.pop(0)
        if val == "#": 
            return None
        node = TreeNode(int(val))
        node.left = self.dfs(der)
        node.right = self.dfs(der)
        return node
        

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