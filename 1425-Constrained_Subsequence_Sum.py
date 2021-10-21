"""
- dynamic programming (top-down)
- O(nk), O(n)
"""
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        
        @lru_cache(None)
        def dp(i): # i - previous chosen index
            nonlocal N
            if i >= N: return 0
            if i == -1: # has to choose one if not chosen
                return max(nums[i] + dp(i) for i in range(N))
            maxx = 0 # maxx when choose none
            for j in range(i + 1, min(i + k + 1, N)):
                maxx = max(maxx, nums[j] + dp(j))
            return maxx
        
        return dp(-1)

"""
- monotonic queue
- deque[i] - decreasing sums ends at i
- O(n), O(n)
"""
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        deque = collections.deque() # decreasing sum
        sums = [0] * len(nums) # max sum till i
        res = nums[0]
        
        for i in range(len(nums)):
            sums[i] = nums[i]
            if deque: sums[i] += sums[deque[0]]
            res = max(res, sums[i])
            if i >= k and deque and deque[0] < i - k + 1:
                deque.popleft()
            while deque and sums[deque[-1]] <= sums[i]:
                deque.pop()
            if sums[i] > 0:
                deque.append(i)

        return res