"""
- brutal force
- O(2**n), O(n)
"""
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sums = [0]
        
        for num in nums:
            curr_sums = []
            for _sum in sums:
                curr_sums.append(_sum + num)
                curr_sums.append(_sum - num)
            sums = curr_sums
        
        result = 0
        for _sum in sums:
            if _sum == target:
                result += 1
        return result

"""
- dp (top-down): dfs(i, _sum) - returns the number of ways for the i index to add to target _sum
- O(n*l), O(n*l) - l: 2000
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        @lru_cache(None)
        def dfs(i, _sum):
            if i < 0:
                return 0
            if i == 0 and (_sum == nums[0] or _sum == -nums[0]):
                return 2 if nums[0] == 0 else 1
            return dfs(i - 1, _sum - nums[i]) + dfs(i - 1, _sum + nums[i])
        
        return dfs(len(nums) - 1, S)

"""
- dp (bottom-up): dp[sum][i] - the number of ways for the i index to add to target sum
- O(n*l), O(n*l) - l: 2000
"""
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(2001)]
        dp[1000][0] = 1
        for i in range(n):
            for _sum in range(-1000, 1001):
                sum_i = _sum + 1000
                if dp[sum_i][i] > 0:
                    if sum_i + nums[i] < 2001:
                        dp[sum_i + nums[i]][i + 1] += dp[sum_i][i]
                    if sum_i - nums[i] >= 0:
                        dp[sum_i - nums[i]][i + 1] += dp[sum_i][i]      
        return dp[target + 1000][n]

"""
- dp (bottom-up): space optimized: only memoization for previous i needed to compute i + 1
- O(n*l), O(n) - l: 2000
"""
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        dp = [0] * 2001
        dp[1000] = 1
        for i in range(n):
            curr_dp = [0] * 2001
            for _sum in range(-1000, 1001):
                sum_i = _sum + 1000
                if dp[sum_i] > 0:
                    if sum_i + nums[i] < 2001:
                        curr_dp[sum_i + nums[i]] += dp[sum_i]
                    if sum_i - nums[i] >= 0:
                        curr_dp[sum_i - nums[i]] += dp[sum_i]
            dp = curr_dp
        return dp[target + 1000]

"""
- dp (bottom-up): optimized: using hashmap
- O(n*l), O(n) - l: 2000
"""
class Solution(object):
    def findTargetSumWays(self, A, S):
        count = collections.Counter({0: 1})
        for x in A:
            step = collections.Counter()
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
        return count[S]