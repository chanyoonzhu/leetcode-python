# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    - dfs + Sort an Almost Sorted Array Where Two Elements Are Swapped
    - O(n), O(n)
    """
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder_traversal = []
        small_node = None
        large_node = None
        
        def dfs(node):
            if node:
                dfs(node.left)
                inorder_traversal.append(node)
                dfs(node.right)
        
        dfs(root)
        # Sort an Almost Sorted Array Where Two Elements Are Swapped
        for i in range(len(inorder_traversal) - 1):
            if inorder_traversal[i + 1].val < inorder_traversal[i].val:
                small_node = inorder_traversal[i + 1]
                if not large_node: # large node only need to find once, small node may need two passes
                    large_node = inorder_traversal[i]
                else:
                    break
                    
        small_node.val, large_node.val = large_node.val, small_node.val
    

    """
    - dfs recursive: store previous node in a global variable as we traverse
    - O(n), O(n)
    """
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.small_node = None
        self.large_node = None
        self.prev = None
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if self.prev and self.prev.val > node.val:
                self.small_node = node
                if not self.large_node:
                    self.large_node = self.prev
                else:
                    return
            self.prev = node
            dfs(node.right)    
        
        dfs(root)
        self.small_node.val, self.large_node.val = self.large_node.val, self.small_node.val


        """same solution using nonlocal"""
        """
        def dfs(node):
            nonlocal small_node, large_node, prev
            if not node:
                return
            dfs(node.left)
            if prev and prev.val > node.val:
                small_node = node
                if not large_node:
                    large_node = prev
                else:
                    return
            prev = node
            dfs(node.right)    
        
        small_node = large_node = prev = None
        dfs(root)
        small_node.val, large_node.val = large_node.val, small_node.val
        """
    
    """
    - dfs iterative: store previous node in a global variable as we traverse
    - O(n), O(n)
    """
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """   
        
        small_node = large_node = prev = None
        
        stack = []
        node = root
        
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev and prev.val > node.val:
                    small_node = node
                    if not large_node:
                        large_node = prev
                    else:
                        break
                prev = node
                node = node.right
        
        small_node.val, large_node.val = large_node.val, small_node.val

    """
    - Morris Traversal
    - Algorithm:
    1. Initialize the root as the current node curr.
    2. While curr is not NULL, check if curr has a left child.
    3. If curr does not have a left child, print curr and update it to point to the node on the right of curr.
    4. Else, make curr the right child of the rightmost node in curr's left subtree.
    5. Update curr to this left node.
    """
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """   
        
        small_node = large_node = prev =  None
        node = root
        
        while node:
            if node.left:
                temp = node.left
                while temp.right and temp.right != node:
                    temp = temp.right
                if not temp.right: # when looking for prev, attach temp.right to node
                    temp.right, node = node, node.left
                    continue
                # when traversal, detach temp.right from node
                temp.right = None
            if prev and prev.val > node.val:
                small_node = node
                if not large_node:
                    large_node = prev
            prev = node
            node = node.right
            
        
        small_node.val, large_node.val = large_node.val, small_node.val