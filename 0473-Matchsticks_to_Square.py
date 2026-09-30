"""
- dp(top-down dfs)
- O(4 ** n), O(n) 
"""
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        side_length, mod = divmod(sum(nums), 4)
        if mod:
            return False
        
        sums = [0] * 4

        nums.sort(reverse=True) # TLE without this line
        def dfs(i):
            if i == len(nums):
                return sums[0] == sums[1] == sums[2] == side_length
            for j in range(4):
                if sums[j] + nums[i] <= side_length:
                    sums[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    sums[j] -= nums[i]
            return False
        
        return dfs(0)

"""
- todo: dp with bit mask
"""