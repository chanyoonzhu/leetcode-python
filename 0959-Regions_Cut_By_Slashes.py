"""
- dfs
- O(n * 2), O(n * 2)
"""
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        """
        - intuition: convert this into an "island" problem: slashes are "water", find how many isolated islands
        - approach: pixelate the n * n grid to 3n * 3n grid (why not 2n * 2n? because connected islands can be diagonal, instead of vertical/horizontal thus hard to track)
        """
        N = len(grid)
        nums = [[0] * (N * 3) for _ in range(N * 3)]
                
        for i in range(N):
            grid[i] = grid[i].replace("\\", "*")
            for j in range(N):
                if grid[i][j] == "/":
                    nums[i * 3][j * 3 + 2] = 1
                    nums[i * 3 + 1][j * 3 + 1] = 1
                    nums[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == "*":
                    nums[i * 3][j * 3] = 1
                    nums[i * 3 + 1][j * 3 + 1] = 1
                    nums[i * 3 + 2][j * 3 + 2] = 1
        
        result = 0
        visited = set()
        
        def dfs(r, c):
            if nums[r][c] != 1 and (r, c) not in visited:
                visited.add((r, c))
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + i, c + j
                    if 0 <= nr < N * 3 and 0 <= nc < N * 3:
                        dfs(nr, nc)
        
        for i in range(N * 3):
            for j in range(N * 3):
                if nums[i][j] == 0 and (i, j) not in visited:
                    dfs(i, j)
                    result += 1
        
        return result


"""
- todo: union find
"""