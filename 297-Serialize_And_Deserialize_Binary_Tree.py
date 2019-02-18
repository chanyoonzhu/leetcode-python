# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    
    """
    - bfs
    def serialize(self, root):
        
        q = [root]
        bfs = []
        
        while q:
            node = q.pop(0)
            if node:
                bfs.append(str(node.val))
            else:
                bfs.append('None')
            if node:
                q.append(node.left)
                q.append(node.right)
              
        while len(bfs) > 0:
            if bfs[-1] == 'None':
                bfs.pop()
            else:
                break
        
        return ','.join(bfs)
                
            
        

    def deserialize(self, data):
        
        if not data:
            return None
        
        bfs = data.split(',')
        for i in range(len(bfs)):
            if bfs[i] == 'None':
                bfs[i] = None
            elif bfs[i][0] == '-':
                bfs[i] = -int(bfs[i][1:])
            else:
                bfs[i] = int(bfs[i])

        if not bfs:
            return None
        
        root = TreeNode(bfs[0])
        level = [root]
        i = 1
        while i < len(bfs):
            copy, level = level[:], []
            for node in copy:
                if i < len(bfs): 
                    if bfs[i] is not None: 
                        node.left = TreeNode(bfs[i])
                        level.append(node.left)
                if i + 1 < len(bfs): 
                    if bfs[i+1] is not None:
                        node.right = TreeNode(bfs[i+1])
                        level.append(node.right)
                i += 2
        return root
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        p = []
        
        def preorder(root):
            if not root:
                p.append('')
            if root:
                p.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
        
        preorder(root)
            
        return ','.join(p)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        p = data.split(',')
        
        def helper(p):
            if not p:
                return None
            val = p[0]
            if not val:
                del p[0]
                return None
            else:
                root = TreeNode(int(p[0]))
                del p[0]
                root.left = helper(p)
                root.right = helper(p)
            return root
        
        return helper(p)
        

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