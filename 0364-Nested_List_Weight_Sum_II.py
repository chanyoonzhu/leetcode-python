# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

"""
- dfs (two passes - get max_depth first)
- O(n), O(n)
"""
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth = self.getMaxDepth(nestedList)
        return self._helper(nestedList, max_depth)
        
    def _helper(self, nestedList: List[NestedInteger], weight: int) -> int:
        total = 0
        for ni in nestedList:
            if ni.isInteger():
                total += ni.getInteger() * weight
            else:
                total += self._helper(ni.getList(), weight - 1)
        return total
    
    def getMaxDepth(self, nestedList: List[NestedInteger]) -> int:
        return 1 + max([self.getMaxDepth(nestedInt.getList()) for nestedInt in nestedList if not nestedInt.isInteger()], default=0)

"""
- dfs (one pass)
- intuition, weight sum = total * max_height - height sum
- O(n), O(n)
"""
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        depth_prod_value, total, max_depth = self.dfs(nestedList, 1)
        return total * (max_depth + 1) - depth_prod_value
        
    def dfs(self, nestedList, depth): # returns: depth * value, sum of all elements, largest height, 
        depth_prod_value = total = max_depth = 0
        for ni in nestedList:
            if ni.isInteger():
                depth_prod_value += depth * ni.getInteger()
                total += ni.getInteger()
                max_depth = max(max_depth, depth)
            else:
                ni_depth_prod_value, ni_total, ni_max_depth = self.dfs(ni.getList(), depth + 1)
                depth_prod_value += ni_depth_prod_value
                total += ni_total
                max_depth = max(max_depth, ni_max_depth)
        return depth_prod_value, total, max_depth