"""
- dp (top-down dfs)
- O(n*d), O(n)
"""
class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        
        dp = [0] * len(arr)
        
        def dfs(i):
            if dp[i]:
                return dp[i]
            curr_max = 1
            for j in range(1, d + 1):
                if i + j >= len(arr) or arr[i + j] >= arr[i]:
                    break
                curr_max = max(curr_max, dfs(i + j) + 1)
            for j in range(1, d + 1):                    
                if i - j < 0 or arr[i - j] >= arr[i]:
                    break
                curr_max = max(curr_max, dfs(i - j) + 1)
            dp[i] = curr_max
            return curr_max
        
        result = 0
        for i in range(len(arr)):
            result = max(result, dfs(i))
        return result

"""
- dp (bottom-up) calculate smaller num first since they won't change
- O(nlogn + n*d), O(n)
"""
class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        dp = [1] * len(arr)
        for num, i in sorted([(num, i) for i, num in enumerate(arr)]):
            for j in range(i + 1, i + d + 1):
                if j >= n or arr[j] >= arr[i]: break
                dp[i] = max(dp[i], dp[j] + 1)
            for j in range(i - 1, i - d - 1, -1):
                if j < 0 or arr[j] >= arr[i]: break
                dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

"""
- todo: O(n) solution with monotonic stack
"""