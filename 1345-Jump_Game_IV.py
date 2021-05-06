"""
- bfs + hashmap
- Time limit exceeded
"""
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp = [float("inf")] * n
        dp[0] = 0
        stack = [0]
        visited = set([0])
        
        value_map = collections.defaultdict(list)
        for i, num in enumerate(arr):
            value_map[num].append(i)
        
        while stack:
            i = stack.pop(0)
            for j in value_map[arr[i]] + [i - 1, i + 1]:
                if j not in visited and 0 <= j < n:
                    dp[j] = min(dp[j], dp[i] + 1)
                    visited.add(j)
                    stack.append(j)
        
        return dp[n - 1]

"""
- bfs + hashmap (optimized)
- Time limit exceeded
"""
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        stack = [(0, 0)]
        visited = set([0])
        
        if n == 1: return 0
        
        value_map = collections.defaultdict(list)
        for i, num in enumerate(arr):
            value_map[num].insert(0, i) # insert larger index in the front since larger index is closer to the end
        
        while stack:
            i, step = stack.pop(0)
            for j in value_map[arr[i]] + [i - 1, i + 1]:
                if j not in visited and 0 <= j < n:
                    if j == n - 1: # return when enqueue, not when dequeue
                        return step + 1
                    visited.add(j)
                    stack.append((j, step + 1))