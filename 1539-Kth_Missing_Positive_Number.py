"""
- Array linear scan
- O(n), O(1)
"""
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        idx = 0
        prev = 0
        while idx < len(arr):
            gap = arr[idx] - prev - 1
            if gap >= k: # easy to miss: equal
                return prev + k
            else:
                k -= gap
            prev = arr[idx]
            idx += 1
        return prev + k


"""
- binary search
- intuition:  The number of positive integers which are missing before the arr[idx] is equal to arr[idx] - (idx + 1). Find index (lo) such that's the last index with missing number < k
- O(logn), O(1)
"""
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
       
        lo, hi = -1, len(arr) - 1 # easy to miss: lo can be -1  [2], 1 -> 1
        
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2

            mid_missing = arr[mid] - (mid + 1)
            if mid_missing >= k:
                hi = mid - 1
            else:
                lo = mid
        if lo == -1:
            return k
        return k + lo + 1 # k - (arr[lo] - lo - 1) + arr[lo]    