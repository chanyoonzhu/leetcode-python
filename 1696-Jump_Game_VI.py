"""
- dp(top-down) dp[i] - max score to end starting from index i
- O(nk), O(n)
- time limit exceeded
"""
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        @lru_cache
        def dp(i): # max points from i to end
            # easy to miss: must end at len(nums) - 1
            if i >= len(nums): return float("-inf")
            if i == len(nums) - 1: return nums[i]
            return max(nums[i] + dp(i + step) for step in range(1, k + 1))
        
        return dp(0)

"""
- dp(bottom-up) dp[i] - max score to end starting from index i
- O(nk), O(n)
- time limit exceeded
"""

class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        dp =[float("-inf")] * N
        dp[0] = nums[0]
        
        for i in range(N):
            for j in range(max(0, i - k), i):
                dp[i] = max(dp[i], nums[i] + dp[j])
        
        return dp[-1]

"""
- dp + priority queue (optimizes when k is large)
- O(n), O(n)
"""
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        result = nums[-1]
        q = [(-nums[-1], n - 1)] # result, i
        
        for i in range(n - 2, -1, -1):
            while q[0][1] > i + k:
                heapq.heappop(q)
            result = -q[0][0] + nums[i]
            heapq.heappush(q, (-result, i))
                
        return result

"""
- dp + monotonic increasing queue (optimizes previous solution)
- O(n), O(n)
- similar question: 239(sliding window)
- algorithm:
 Iterate over nums. For each element nums[i]:
    - Pop all the indexes larger than i+k out of dq from left.
    - Update score[i] to score[dq.peekFirst()] + nums[i].
    - If the corresponding score of the rightmost index in dq (i.e., score[dq.peekLast()]) is smaller than score[i], pop it from the right to make corresponding values monotonically decreasing. Repeat.
    - Push i into the right of dq.
"""
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[-1] = nums[-1]
        next_candidate_index = [n - 1] # a monotonically decreasing queue
        
        for i in range(n - 2, -1, -1):
            while next_candidate_index and next_candidate_index[0] > i + k:
                next_candidate_index.pop(0)
            dp[i] = nums[i] + dp[next_candidate_index[0]]
            while next_candidate_index and dp[next_candidate_index[-1]] <= dp[i]:
                next_candidate_index.pop()
            next_candidate_index.append(i)        
        return dp[0]

"""
- monotonic queue
- O(n), O(k)
"""
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q = collections.deque([0]) # mono-decreasing queue
        N = len(nums)

        for i in range(1, N):
            while q and q[0] < i - k: q.popleft()
            nums[i] += nums[q[0]]   
            while q and nums[i] >= nums[q[-1]]: q.pop()
            q.append(i)
            
        return nums[-1]