"""
- binary search
- O(nlogn), O(1)
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        lo, hi = 0, len(nums) - 1
        
        def get_smaller_count(x):
            count = 0
            for n in nums:
                if n <= x:
                    count += 1
            return count
        
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if get_smaller_count(mid) <= mid:
                lo = mid + 1
            else:
                hi = mid
        return lo

"""
- bitmask
- O(nlog(n))
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        bits = 0
        for n in nums:
            if bits >> n & 1:
                return n
            bits |= 1 << n 
        