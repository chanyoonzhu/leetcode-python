from collections import deque
from typing import List


"""
- bfs
- O(mn), O(mn)
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        M, N = len(grid), len(grid[0])
        total_orange = rotten_orange = 0
        q = deque()
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    total_orange += 1
                elif grid[r][c] == 1:
                    total_orange += 1
        
        time = 0
        while q:
            r, c, time = q.popleft()
            rotten_orange += 1
            for i, j in DIR:
                nr, nc = r + i, c + j
                if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, time + 1))
        
        if rotten_orange == total_orange:
            return time
        return -1


class Solution:
    """Added September 2026: multi-source BFS without mutating the grid.

    Track fresh oranges in a separate set and remove each one when it is first
    reached. Process the queue one minute-layer at a time.

    Complexity:
        Time: O(rows * cols), since each cell is examined a constant number of times.
        Space: O(rows * cols) for the queue and fresh-orange set.
    """

    _DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh.add((row, col))

        minutes = 0
        while queue and fresh:
            # visit all fresh oranges 1 step away
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for row_delta, col_delta in self._DIRECTIONS:
                    next_row = row + row_delta
                    next_col = col + col_delta
                    next_cell = (next_row, next_col)
                    in_bounds = 0 <= next_row < rows and 0 <= next_col < cols
                    if in_bounds and next_cell in fresh:
                        fresh.remove(next_cell)
                        queue.append(next_cell)
            minutes += 1

        return minutes if not fresh else -1

    # Interview test cases, grouped by behavior:
    # Core propagation:
    #   - [[2, 1, 1], [1, 1, 0], [0, 1, 1]] -> 4.
    #   - [[2, 1, 1], [0, 1, 1], [1, 0, 1]] -> -1 (one fresh orange is unreachable).
    # Starting states:
    #   - [[0, 2]] -> 0 (no fresh oranges).
    #   - [[1]] -> -1 (fresh orange but no rotten source).
    # Boundaries and shape:
    #   - [[2]] -> 0; [[1, 1, 1]] -> -1.
    #   - [] and [[]] -> 0 (defensive cases).
    # Input preservation:
    #   - The core propagation case returns 4 and leaves the input grid unchanged.
