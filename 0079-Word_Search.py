# Clarification questions for Word Search (79):
# - Are only horizontal and vertical neighbors adjacent? Yes; diagonal moves do not count.
# - Can one board cell be used more than once in a word? No.
# - May the board or word be empty? The constraints exclude this; the added
#   solution handles empty inputs defensively.
# - What characters are allowed? Uppercase and lowercase English letters.
# - Should the search mutate the board? The added solution leaves it unchanged.

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        """
        - O(mn ^ 2), O(mn)
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set([])
                if self.dfs(board, i, j, word, visited):
                    return True
        return False
    
    def dfs(self, board, i, j, word, visited):
        if board[i][j] != word[0]:
            return False
        elif len(word) == 1:
            return True
        else:
            m, n = len(board), len(board[0])
            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            result = False
            wordRemain = word[1:]
            visited.add((i,j))
            for di,dj in directions:
                nexti, nextj = i+di, j+dj
                if (nexti, nextj) not in visited and 0 <= nexti < m and 0 <= nextj < n:
                    result = result or self.dfs(board, nexti, nextj, wordRemain, visited)
            visited.remove((i,j)) ## easy to forget!
            return result
        """
        
        """
        - O(mn ^ 2), O(1)
        - change board to mark visited
        """
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False
    
    def dfs(self, board, i, j, word):
        if board[i][j] != word[0]:
            return False
        elif len(word) == 1:
            return True
        else:
            m, n = len(board), len(board[0])
            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            result = False
            wordRemain = word[1:]
            thisChar = board[i][j]
            board[i][j] = '#'
            for di,dj in directions:
                nexti, nextj = i+di, j+dj
                if 0 <= nexti < m and 0 <= nextj < n and board[nexti][nextj] != "#":
                    result = result or self.dfs(board, nexti, nextj, wordRemain)
            board[i][j] = thisChar
            return result


class Solution:
    """Added September 2026: indexed DFS with a path-local visited set.

    The index avoids allocating a new suffix string at each recursive call.
    Visited cells are removed on backtracking, and the board is never modified.

    Complexity:
        Time: O(M * N * 3^L) worst case, where L is the word length.
        Space: O(L) for the recursion stack and path-local visited set.
    """

    _DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])
        if len(word) > rows * cols:
            return False

        visited: set[tuple[int, int]] = set()

        return any(
            self._dfs(board, row, col, word, 0, visited)
            for row in range(rows)
            for col in range(cols)
        )

    def _dfs(
        self,
        board: List[List[str]],
        row: int,
        col: int,
        word: str,
        index: int,
        visited: set[tuple[int, int]],
    ) -> bool:
        if (row, col) in visited or board[row][col] != word[index]:
            return False
        if index == len(word) - 1:
            return True

        rows, cols = len(board), len(board[0])
        visited.add((row, col))
        found = False
        for row_delta, col_delta in self._DIRECTIONS:
            next_row = row + row_delta
            next_col = col + col_delta
            if (
                0 <= next_row < rows
                and 0 <= next_col < cols
                and self._dfs(
                    board,
                    next_row,
                    next_col,
                    word,
                    index + 1,
                    visited,
                )
            ):
                # don't immediately return since we need to remove from visited for correct backtracking
                found = True
                break
        visited.remove((row, col)) # easy to forget!
        return found


# Interview test cases for Word Search (79), grouped by behavior:
# Standard matches:
#   - The example board with "ABCCED" -> True.
#   - The example board with "SEE" -> True.
# Reuse and non-matches:
#   - The example board with "ABCB" -> False; completing it would reuse a cell.
#   - A word containing a letter absent from the board -> False.
# Boundaries:
#   - One cell board [["A"]], word "A" -> True; word "B" -> False.
#   - Empty word -> True; empty board with a nonempty word -> False (defensive cases).
#   - Word longer than the number of board cells -> False.
# Input preservation:
#   - The added indexed solution leaves the board unchanged after success or failure.
