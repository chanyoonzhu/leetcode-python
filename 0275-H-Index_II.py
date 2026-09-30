"""
- Better definition: The h-index is defined as the maximum value of h such that the given author/journal has published h papers that have each been cited at least h times.
"""

"""
- linear search
- O(n), O(n)
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        for i in range(n, 0, -1):
            if citations[n - i] >= i:
                return i
        return 0 # edge case all zero reference -> 0

"""
- binary search
- O(logn), O(n)
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lowest, highest = 0, n
        while lowest < highest:
            mid = lowest + (highest - lowest + 1) // 2
            if mid <= citations[n - mid]:
                lowest = mid
            else:
                highest = mid - 1
        return lowest