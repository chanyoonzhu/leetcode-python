"""
- dp (top-down), dp[i1][i2][isEmpty] - the max dot product for nums1[:i1 + 1] and nums2[:i2 + 1] isEmpty: whether subsequence is empty
- O(mn), O(mn)
"""
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i1, i2, isEmpty):
            if i1 == self.n1 or i2 == self.n2:
                if isEmpty: 
                    return self.max
                else:
                    return 0
            prod = nums1[i1] * nums2[i2]
            self.max = max(self.max, prod)
            return max(prod + dp(i1 + 1, i2 + 1, False), dp(i1 + 1, i2, isEmpty), dp(i1, i2 + 1, isEmpty))
        
        self.max = float("-inf") # single prod max
        self.n1, self.n2 = len(nums1), len(nums2)
        
        return dp(0, 0, True)


"""
- dp (bottom-up), dp[i1][i2][isEmpty] - the max dot product for nums1[:i1 + 1] and nums2[:i2 + 1] isEmpty: whether subsequence is empty
- O(mn), O(mn)
"""
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1, n2 = len(nums1), len(nums2)
        dp = [[[0, False] for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        max_prod = float("-inf")
        for i1 in range(1, n1 + 1):
            for i2 in range(1, n2 + 1):
                prod = nums1[i1 - 1] * nums2[i2 - 1]
                max_prod = max(max_prod, prod)
                result_use_current_chars = prod + dp[i1 - 1][i2 - 1][0]
                if result_use_current_chars >= max(dp[i1][i2 - 1][0], dp[i1 - 1][i2][0]):
                    dp[i1][i2] = (result_use_current_chars, True)
                elif dp[i1][i2 - 1][0] >= dp[i1 - 1][i2][0]:
                    dp[i1][i2] = dp[i1][i2 - 1]
                else:
                    dp[i1][i2] = dp[i1 - 1][i2]
        return dp[-1][-1][0] if dp[-1][-1][1] else max_prod

"""
- dp (bottom-up), dp[i1][i2] - the max dot product for nums1[:i1 + 1] and nums2[:i2 + 1], empty case handled seperately
- O(mn), O(mn)
"""
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        n1, n2 = len(nums1), len(nums2)
		
        if (max(nums1) < 0 and min(nums2) > 0):
            return max(nums1) * min(nums2) 
        if (max(nums2) < 0 and min(nums1) > 0):
            return min(nums1) * max(nums2)         
			
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i1 in range(1, n1 + 1):
            for i2 in range(1, n2 + 1):
                dp[i1][i2] = max(dp[i1 - 1][i2 - 1] + nums1[i1 - 1] * nums2[i2 - 1], dp[i1][i2 - 1], dp[i1 - 1][i2])
        return dp[-1][-1]

"""
- dp (bottom-up), space optimized
- O(mn), O(m)
"""
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1, n2 = len(nums1), len(nums2)
		
        if (max(nums1) < 0 and min(nums2) > 0):
            return max(nums1) * min(nums2) 
        if (max(nums2) < 0 and min(nums1) > 0):
            return min(nums1) * max(nums2)         
			
        dp_prev = [0 for _ in range(n2 + 1)]
        for i1 in range(1, n1 + 1):
            dp = [0 for _ in range(n2 + 1)]
            for i2 in range(1, n2 + 1):
                dp[i2] = max(dp_prev[i2 - 1] + nums1[i1 - 1] * nums2[i2 - 1], dp[i2 - 1], dp_prev[i2])
            dp_prev = dp
        return dp[-1]

"""
- dp (bottom-up), optimized: overwrite 0 with max_prod
- O(mn), O(m)
- https://leetcode.com/problems/max-dot-product-of-two-subsequences/discuss/648420/JavaC%2B%2BPython-the-Longest-Common-Sequence
"""
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n2) for i in range(n1)]
        for i in range(n1):
            for j in range(n2):
                dp[i][j] = nums1[i] * nums2[j]
                if i and j: dp[i][j] += max(dp[i - 1][j - 1], 0)
                if i: dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j: dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[-1][-1]