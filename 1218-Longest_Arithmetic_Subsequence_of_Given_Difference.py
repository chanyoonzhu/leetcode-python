"""
- dynamic programming
- dp(i) - Longest Arithmetic Subsequence of Given Difference ending at index i (i needs to be included)
- O(n^2), O(n)
"""
class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        
        @lru_cache(None)
        def dp(i):
            if i < 0:
                return 0
            count = 1
            for k in range(i-1, -1, -1):
                if arr[k] + difference == arr[i]:
                    count += dp(k)
                    break # greedily match the first satisfying
            return count
        
        return max(dp(i) for i in range(len(arr)))

"""
- dynamic programming (buttom-up)
- O(n), O(n)
"""
class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        
        dp = [1] * len(arr)
        number_last_pos = {}
        res = 1
        
        for i, x in enumerate(arr):
            if x - difference in number_last_pos:
                dp[i] = dp[number_last_pos[x - difference]] + 1
                res = max(res, dp[i])
            number_last_pos[x] = i
        return res

"""
- hashmap
- O(n), O(n)
"""
class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        
        memo = {}
        for x in arr:
            memo[x] = memo[x-difference] + 1 if x-difference in memo else 1
            
        return max(memo.values())

"""
- follow-up: difference can be from 1 to difference (where difference > 0)

"""
class SolutionFollowUp:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        
        dp = [1] * len(arr)
        number_last_pos = {}
        res = 1
        
        for i, x in enumerate(arr):
            for diff in range(1, difference + 1):
                if x - diff in number_last_pos:
                    dp[i] = max(dp[i], dp[number_last_pos[x - diff]] + 1)
                    res = max(res, dp[i])
            number_last_pos[x] = i
        return res

s = SolutionFollowUp()
print(s.longestSubsequence([3, 1, 2, 5, 8, 13, 10], 3)) # 5 => [1， 2， 5， 8， 10]