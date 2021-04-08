class Solution:

    """
    - dfs with memoization
    - O(mn), O(mn)
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def dfs(x, y, longest):
            for i, j in move:
                x_next = x + i
                y_next = y + j
                if 0 <= x_next < n and 0 <= y_next < m and matrix[x_next][y_next] > matrix[x][y]:
                    next_longest_path = longest_paths[x_next][y_next] if (x_next, y_next) in visited else dfs(x_next, y_next, 1)
                    longest = max(longest, next_longest_path + 1)
            visited.add((x, y))
            longest_paths[x][y] = longest
            return longest
            
        
        n, m = len(matrix), len(matrix[0])
        longest_paths = [[1] * m for _ in range(n)]
        visited = set()
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = 0
        
        for i in range(n):
            for j in range(m):
                result = max(result, dfs(i, j, 1))
        return result
    
    """
    - topological sorting # todo
    """