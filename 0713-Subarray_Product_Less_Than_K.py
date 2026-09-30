"""
- prefix product
- O(n), O(n)
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prefix_product = [1]
        for x in nums:
            prefix_product.append(prefix_product[-1] * x)
            
        N = len(prefix_product)
            
        res = 0
        left = 0
        for right in range(1, N):
            while left < right and prefix_product[right] / prefix_product[left] >= k:
                left += 1
            res += (right - left)
        return res

"""
- sliding window
- O(n), O(n)
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        N = len(nums)
        left = res = 0
        curr = 1
        for right in range(N):
            curr *= nums[right]
            while left <= right and curr >= k: # easy to miss: left <= right otherwise go out of bound when k == 0
                curr /= nums[left]
                left += 1
            res += (right - left + 1)
            
        return res