"""
- dynamic programming (with bitmasking)
- O(2^m * m)
"""
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        M = len(nums1)
        memo = {}
        
        def dp(i, bit_state):
            if i == M:
                return 0
            if bit_state not in memo:
                min_sum = float("inf")
                for j in range(M):
                    if bit_state & (1 << j):
                        min_sum = min(min_sum, (nums1[i] ^ nums2[j]) + dp(i + 1, bit_state ^ (1 << j)))        
                memo[bit_state] = min_sum
            return memo[bit_state]
        
        return dp(0, (1 << M) - 1)
            
        