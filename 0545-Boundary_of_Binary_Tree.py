# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []
        self.preorder(root, res, True, True)
        return res
        
    def preorder(self, node, res, isLeft, isRight):
        if not node: return
        isLeafOrLeft = (not node.left and not node.right) or isLeft
		# append leaf or leftboundary
        if isLeafOrLeft: res.append(node.val)
		# preorder traversal
        if not node.left and not node.right:
            return
        elif not node.right:
            self.preorder(node.left, res, isLeft, isRight and not isLeft)
        elif not node.left:
            self.preorder(node.right, res, isLeft and not isRight, isRight)
        else: 
            self.preorder(node.left, res, isLeft, False)
            self.preorder(node.right, res, False, isRight)
		# append right boundary
        if isRight and not isLeafOrLeft: res.append(node.val)
    

n1 = TreeNode(1)
n1.right = TreeNode(2)
n1.right.left = TreeNode(3)
n1.right.right = TreeNode(4)

print(Solution().boundaryOfBinaryTree(n1))