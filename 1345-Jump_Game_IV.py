"""
- bfs + hashmap
- O(n), O(n)
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
- O(n), O(n)
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
            del value_map[arr[i]] # remove already reversed

"""
- birectional bfs
- O(n), O(n)
"""
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {} # stores same value
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs, other = set([0]), set([n-1])  # store layers from beginning and the end
        visited = {0, n-1}
        step = 0

        # when current layer exists
        while curs:
            # search from the side with fewer nodes
            if len(curs) > len(other):
                curs, other = other, curs
            nex = set()

            # iterate the layer
            for node in curs:

                # check same value
                for child in graph[arr[node]] + [node-1, node+1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.add(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

            curs = nex
            step += 1

        return -1