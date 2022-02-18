# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    if version == 4: # change to the actual first bad version 
        return True
    return False

class Solution(object):
    """
    - binary search recursive
    - O(logn), O(1)
    """
    def firstBadVersion_recursive(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binary_search(1, n + 1)
        
    def binary_search(self, left, right):
        if left == right:
            return left
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
        return self.binary_search(left, right)
    
    """
    - binary search iterative
    - O(logn), O(1)
    """
    def firstBadVersion_iterative(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n + 1
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left



s = Solution()
s.firstBadVersion_recursive(5)

"""
isBadVersion(start, end) -> bool
"""
"""
find all bad versions given above API
"""
class SolutionFollowUp:
    def allBadVersion(self, n):
        self.helper(1, n) ## todo

    def helper(self, start, end):
        if start < end or not isBadVersion(start, end):
            return []
        if isBadVersion(start, start) and isBadVersion(end, end):
            return list(range(start, end + 1))
        mid = start + (end - start) // 2
        l_bads = self.helper(start, mid-1)
        r_bads = self.helper(mid, end)
        if l_bads or r_bads:
            return l_bads or r_bads
        else:
            return l_bads + r_bads
        
        