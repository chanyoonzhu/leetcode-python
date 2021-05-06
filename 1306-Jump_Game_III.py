"""
- similar problem: number of islands series
- instinct: the 2D version of number of islands
"""
"""
- dfs
- O(n), O(n)
"""
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        visited = set()
        
        def dfs(i):
            if 0 <= i < len(arr):
                if arr[i] == 0:
                    return True
                if i not in visited:
                    visited.add(i)
                    return dfs(i + arr[i]) or dfs(i - arr[i])
            return False
        
        return dfs(start)

"""
- bfs
- O(n), O(n)
"""
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        stack = [start]
        visited = set([start])
        
        while stack:
            i = stack.pop(0)
            if arr[i] == 0:
                return True
            front, back = i - arr[i], i + arr[i]
            if front >= 0 and front not in visited:
                stack.append(front)
                visited.add(front)
            if back < len(arr) and back not in visited:
                stack.append(back)
                visited.add(back)
            """ simplified:
            for j in (i - arr[i], i + arr[i]):
                if 0 <= j < len(arr):
                    stack.append(j)
                    visited.add(j)
            """
        
        return False