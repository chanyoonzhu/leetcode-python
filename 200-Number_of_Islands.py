"""
- dfs
- O(mn), O(mn): space can be optimized by mutating the original grid (changing "1" to "#" after visiting)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        M, N = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal M, N
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                rr, cc = r + i, c + j
                if 0 <= rr < M and 0 <= cc < N and (rr, cc) not in visited and grid[r][c] == "1":
                    visited.add((rr, cc))
                    dfs(rr, cc)
        
        for r in range(M):
            for c in range(N):
                if (r, c) not in visited and grid[r][c] == "1":
                    visited.add(r, c)
                    count += 1
                    dfs(r, c)
        return count

"""
- bfs
- O(mn), O(mn): space can be optimized by mutating the original grid (changing "1" to "#" after visiting)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        M, N = len(grid), len(grid[0])
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def traverse(r, c):
            grid[r][c] = "X"
            for i, j in DIR:
                nr, nc = r + i, c + j
                if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] == "1":
                    traverse(nr, nc)
            
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    res += 1
                    traverse(i, j)
        return res


class Solution:
    """Added September 2026: iterative DFS with a visited set and explicit stack.

    Complexity:
        Time: O(rows * cols), since each cell is checked and visited at most once.
        Space: O(rows * cols) for the visited set and traversal stack.
    """

    _DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1" and (x, y) not in visited:
                    islands += 1
                    self._visit_island(grid, x, y, rows, cols, visited)
        return islands

    def _visit_island(
        self,
        grid: List[List[str]],
        start_row: int,
        start_col: int,
        rows: int,
        cols: int,
        visited: set[tuple[int, int]],
    ) -> None:
        stack = [(start_row, start_col)]
        visited.add((start_row, start_col))

        while stack:
            x, y = stack.pop()
            for row_delta, col_delta in self._DIRECTIONS:
                next_x = x + row_delta
                next_y = y + col_delta
                in_bounds = 0 <= next_x < rows and 0 <= next_y < cols
                is_unvisited_land = (
                    in_bounds
                    and (next_x, next_y) not in visited
                    and grid[next_x][next_y] == "1"
                )
                if is_unvisited_land:
                    visited.add((next_x, next_y))
                    stack.append((next_x, next_y))

    # Interview test cases, grouped by behavior:
    # Core connectivity:
    #   - One connected island: [["1", "1"], ["1", "1"]] -> 1.
    #   - Several non-adjacent islands: [["1", "0", "0"], ["0", "0", "1"]] -> 2.
    #   - Land connected only diagonally: [["1", "0"], ["0", "1"]] -> 2.
    # All-water and all-land grids:
    #   - All water: [["0", "0"], ["0", "0"]] -> 0.
    #   - All land: [["1", "1"], ["1", "1"]] -> 1.
    # Shapes and boundaries:
    #   - Single land cell: [["1"]] -> 1.
    #   - Single water cell: [["0"]] -> 0.
    #   - One row: [["1", "0", "1"]] -> 2.
    #   - One column: [["1"], ["0"], ["1"]] -> 2.
    #   - Empty grid [] and empty first row [[]] -> 0 (defensive cases).
    # Large input:
    #   - A large connected island verifies iterative traversal avoids recursion limits.
