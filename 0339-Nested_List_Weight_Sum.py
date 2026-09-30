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
https://leetcode.com/problems/nested-list-weight-sum/
- dfs
- O(n), O(n)
"""
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.helper(nestedList, 1)
            
    def helper(self, nestedList: NestedInteger, depth: int) -> int:
        if not nestedList:
            return 0
        total = 0
        for ni in nestedList:
            if ni.isInteger():
                total += ni.getInteger() * depth
            else:
                total += self.helper(ni.getList(), depth + 1)
        return total

"""
- bfs
- O(n), O(n)
"""
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        q = [(ni, 1) for ni in nestedList] # ni, depth
        res = 0
        
        while q:
            ni, depth = q.pop(0)
            if ni.isInteger():
                res += ni.getInteger() * depth
            else:
                q.extend([(ni, depth + 1) for ni in ni.getList()])
        return res