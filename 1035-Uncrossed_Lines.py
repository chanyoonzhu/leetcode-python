"""
- dp (top-down), dp[i1][i2] - the max connections between nums1[:i1 + 1] to nums2[:i2 + 1]
- O(mn), O(mn)
"""
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        self.n1, self.n2 = len(nums1), len(nums2)
        
        @lru_cache(None)
        def dp(i1, i2):
            if i1 == self.n1 or i2 == self.n2:
                return 0
            _max = max(dp(i1 + 1, i2), dp(i1, i2 + 1))
            if nums1[i1] == nums2[i2]:
                _max = max(_max, 1 + dp(i1 + 1, i2 + 1))
            return _max
        
        return dp(0, 0)

"""
- dp (bottom-up), dp[i1][i2] - the max connections between nums1[:i1 + 1] to nums2[:i2 + 1]
- O(mn), O(mn)
"""
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i1 in range(1, n1 + 1):
            for i2 in range(1, n2 + 1):
                _max = max(dp[i1 - 1][i2], dp[i1][i2 - 1])
                if nums1[i1 - 1] == nums2[i2 - 1]:
                    _max= max(_max, 1 + dp[i1 - 1][i2 - 1])
                dp[i1][i2] = _max
        return dp[-1][-1]

"""
- dp (bottom-up), space optimized
- O(mn), O(n)
"""
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1, n2 = len(nums1), len(nums2)
        dp_prev = [0] * (n2 + 1)
        
        for i1 in range(1, n1 + 1):
            dp = [0] * (n2 + 1)
            for i2 in range(1, n2 + 1):
                _max = max(dp_prev[i2], dp[i2 - 1])
                if nums1[i1 - 1] == nums2[i2 - 1]:
                    _max= max(_max, 1 + dp_prev[i2 - 1])
                dp[i2] = _max
            dp_prev = dp
        return dp[-1]