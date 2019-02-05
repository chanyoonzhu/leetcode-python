# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        def searchRoot(rootIdxPreorder, leftInorder, rightInorder):
            rootIdxInorder = leftInorder
            while rootIdxInorder <= rightInorder:
                if inorder[rootIdxInorder] == preorder[rootIdxPreorder]:
                    return rootIdxInorder
                rootIdxInorder += 1
    
        def recBuild(leftInorder, rightInorder, rootIdxPreorder):
            if leftInorder > rightInorder:
                return None
            rootIdxInorder = searchRoot(rootIdxPreorder, leftInorder, rightInorder)
            root = TreeNode(inorder[rootIdxInorder])
            leftLength = rootIdxInorder - leftInorder
            leftChild = recBuild(leftInorder, rootIdxInorder - 1, rootIdxPreorder + 1)
            rightChild = recBuild(rootIdxInorder + 1, rightInorder, rootIdxPreorder + leftLength + 1)
            root.left = leftChild
            root.right = rightChild
            return root
            
        return recBuild(0, len(inorder)-1, 0)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sl = Solution()
sl.buildTree(preorder, inorder)