class Solution:
    """
    - dynamic programming (top-down)
    - O(n^2*m), O(n^2*m)
    - time limit exceeded
    """
    def splitArray(self, nums: List[int], m: int) -> int:       
        @lru_cache(None)
        def dfs(l, r, count):
            min_sum = sum(nums[l:r + 1])
            if count == 1:
                return min_sum
            for i in range(l, r + 1):
                min_sum = min(min_sum, max(dfs(l, i, 1), dfs(i + 1, r, count - 1)))
            return min_sum
            
        return dfs(0, len(nums) - 1, m)
    
    """
    - dynamic programming (bottom-up)
    - O(n^2*m), O(n*m)
    - time limit exceeded
    """
    def splitArray(self, nums: List[int], m: int) -> int:       
        
        n = len(nums)
        sub = [0] * (n + 1)
        for i in range(n):
            sub[i + 1] = sub[i] + nums[i]
        
        dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sub[i] - sub[k]))
        
        return dp[n][m]
    
    """
    - binary search + greedy
    - O(nlogk) - k is the sum of array, O(1)
    """
    def splitArray(self, nums: List[int], m: int) -> int:       
        
        _sum = sum(nums)
        
        def binary_search(l, r):
            if l == r:
                return l
            mid = l + (r - l) // 2
            if canSplit(mid):
                return binary_search(l, mid)
            else:
                return binary_search(mid + 1, r)          
        
        def canSplit(subsum):
            curr_subsum = 0
            splitted = 0
            for num in nums:
                if num > subsum:
                    return False
                curr_subsum += num
                if curr_subsum > subsum:
                    splitted += 1
                    curr_subsum = num
                    if splitted == m:
                        return False
            return True
        
        return binary_search(0, _sum)