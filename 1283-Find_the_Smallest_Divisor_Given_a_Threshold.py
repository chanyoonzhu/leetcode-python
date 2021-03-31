class Solution:
    """
    - binary search
    - O(nlogK) K - nums max, O(1)
    """
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_possible = max(nums)
        
        def binary_search(l, r):
            if l == r:
                return l
            mid = l + (r - l) // 2
            if satisfy_threshold(mid):
                return binary_search(l, mid)
            else:
                return binary_search(mid + 1, r)
        
        def satisfy_threshold(divisor):
            sums = 0
            for num in nums:
                sums += ceil(num / divisor)
                if sums > threshold:
                    return False
            return True
        
        return binary_search(1, max_possible)