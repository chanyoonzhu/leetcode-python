class Solution(object):
    """
    - greedy, sweep lines
    - O(nlogn), O(n) - sorting, space can be O(1) based on API used
    - Algorithm: 
    1. sort by start time
    2. when overlapping, always remove the one ends later - greedy
    3. return total removed
    """
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x:x[0])
        prev_end = float("-inf")
        removed = 0
        for start, end in intervals:
            if start < prev_end:
                if end <= prev_end:
                    prev_end = end
                removed += 1
            else:
                prev_end = end
        return removed

    """
    - dynamic programming - top down
    - dp[i]: the maximum number of valid intervals that can be included in the final list if the intervals upto the ith interval, dp[i+1]=max(dp[j])+1
    - O(n*2), O(n)
    - time limit exceeded
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        dp = [-1] * len(intervals)
        dp[0] = 1
        
        def dfs(dp, idx):
            if dp[idx] != -1:
                return dp[idx]
            max_kept = float("-inf")
            for i in range(idx):
                kept = dfs(dp, i)
                if intervals[i][1] <= intervals[idx][0]:
                    kept += 1
                max_kept = max(max_kept, kept)
            dp[idx] = max_kept
            return max_kept
        
        intervals = sorted(intervals, key=lambda x: x[0])
        dfs(dp, len(intervals) - 1)
        return len(intervals) - dp[-1]

    """
    - dynamic programming - bottom up
    - dp[i]: the maximum number of valid intervals that can be included in the final list if the intervals upto the ith interval, dp[i+1]=max(dp[j])+1
    - O(n*2), O(n)
    - time limit exceeded
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        n = len(intervals)
        dp = [0] * n
        dp[0] = 1
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        for i in range(1, n):
            max_kept = 0
            for j in range(i):
                kept = dp[j]
                if intervals[i][0] >= intervals[j][1]:
                    kept += 1
                max_kept = max(max_kept, kept)
            dp[i] = max_kept
                
        return len(intervals) - dp[-1]

s = Solution()
s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])