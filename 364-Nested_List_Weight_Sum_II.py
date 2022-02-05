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
- O(n), O(n)
"""
"""
- todo: improve - 算个所有array 的 sum，到最后，sum*depth - 那个正向求和的总数
"""
class Solution:
    def __init__(self):
        self.depth_to_sum = collections.defaultdict(int)
        
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth = self.dfs(nestedList, 1)
        res = 0
        for depth, count in self.depth_to_sum.items():
            res += count * (max_depth - depth + 1)
        return res
        
    def dfs(self, nestedList, depth):
        if not nestedList:
            return 0
        cur_depth = depth
        for ni in nestedList:
            if ni.isInteger():
                self.depth_to_sum[cur_depth] += ni.getInteger()
            else:
                depth = max(depth, self.dfs(ni.getList(), cur_depth + 1))
        return depth