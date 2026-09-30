"""
- bfs
- O(n^2), O(n^2)
"""
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        board_1d = self.convertBoard(board)
        N = len(board_1d)
        
        queue = deque()
        queue.append((1, 0)) # number, step
        visited = set()
        visited.add(1)
            
        while queue:
            cell, step = queue.popleft()
            if cell == N - 1:
                return step
            
            for i in range(1, 7):
                next_ = cell + i
                if self.canVisit(next_, visited, N):
                    visited.add((next_))
                    if board_1d[next_] != -1:
                        # if self.canVisit(board_1d[next_], visited, N):
                        queue.append((board_1d[next_], step + 1))
                        # visited.add(board_1d[next_]) # easy to be wrong: cannot add to visited now! Having this line prevents traversing the ladder when there's one starting at board_1d[next_]
                    else:
                        queue.append((next_, step + 1))
        return -1
                    
    def convertBoard(self, board):
        n = len(board)
        board_1d = [0] * (n ** 2 + 1)
        for r in range(n):
            for c in range(n):
                idx = (n-1-r)*n+c+1 if (n-1-r) % 2 == 0 else (n-1-r)*n+(n-1-c)+1 # easy to be wrong: zigzag
                board_1d[idx] = board[r][c]
        return board_1d
    
    def canVisit(self, cell, visited, size):
        if cell >= size:
            return False
        return cell not in visited

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        """
        - caveat: zigzag mapping
        - slide rule: must slide and can only slide once
        """

        """
        - dfs: key word - shortest path
        - a queue, a visited
        """
            
        n = len(board)
        q = [(0, 1)]
        visited = [0] * (n * n)
        visited[0] = 1
        while q:
            step, square = q.pop(0)
            if square == n * n:
                return step
            for k in range(1, 7):  
                if square + k <= n * n and not visited[square+k-1]:
                    visited[square+k-1] = 1
                    i, j = self.idxConversion(square+k, board)
                    if board[i][j] > 0:
                        q.append((step+1, board[i][j]))
                    else:
                        q.append((step+1, square+k))
        return -1
            
    def idxConversion(self, squareNo, board):
        n = len(board)
        i = n - 1 - (squareNo - 1) // n
        j = (squareNo - 1) % n if i % 2 != n % 2 else n - 1 - (squareNo - 1) % n
        return (i, j)
        

# print(Solution().snakesAndLadders([
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,13,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,15,-1,-1,-1,-1]]))

# print(Solution().snakesAndLadders([
#     [1,1,-1],
#     [1,1,1],
#     [-1,1,1]]))

print(Solution().snakesAndLadders(
    [[-1,-1,19,10,-1],
    [2,-1,-1,6,-1],
    [-1,17,-1,19,-1],
    [25,-1,20,-1,-1],
    [-1,-1,-1,-1,15]]
))