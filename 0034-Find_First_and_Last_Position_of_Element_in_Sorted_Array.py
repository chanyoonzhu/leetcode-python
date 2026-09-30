"""
- binary search
- two passes, one for left boundary, one for right boundary
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearchLeft(A, x):
            l, r = 0, len(A) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if x > A[mid]: l = mid + 1
                else: r = mid - 1
            return l

        def binarySearchRight(A, x):
            l, r = 0, len(A) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if x >= A[mid]: l = mid + 1
                else: r = mid - 1
            return r
        
        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]