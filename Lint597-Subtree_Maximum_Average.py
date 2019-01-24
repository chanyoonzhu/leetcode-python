class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    # class variable
    total = size = 0 
    maxNode = None
    
    def findSubtree2(self, root):
        # write your code here
    
        def helper(root):
            
            if not root:
                return 0, 0
            
            lsum, lsize = helper(root.left)
            rsum, rsize = helper(root.right)
            
            total = lsum + rsum + root.val
            size = lsize + rsize + 1
            
            if (not self.maxNode) or (self.total * size < self.size * total):
                self.maxNode = root
                self.total = total
                self.size = size

            return total, size
        
        helper(root)
        return self.maxNode