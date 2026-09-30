# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- bfs
- init: O(n), O(n); insert: O(1), O(1)
"""
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = []
        self._bfs()
        
    def _bfs(self):
        temp_q = [self.root]
        while temp_q:
            node = temp_q.pop(0)
            if not node.left or not node.right:
                self.q.append(node)
            if node.left: temp_q.append(node.left)
            if node.right: temp_q.append(node.right) 

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        node = self.q[0]
        if not node.left:
            node.left = new_node
        else:
            node.right = new_node
            self.q.pop(0)
        self.q.append(new_node)
        return node.val
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()