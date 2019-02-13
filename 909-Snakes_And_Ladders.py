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

        """
        dp - not a good idea, does not work, why?

        n = len(board)
        dp = [[n+1] * n for _ in range(n)] 
        dp[n-1][0] = 0
        for k in range(2, n*n+1):
            steps = (k - 2) // 6 + 1
            i, j = self.idxConversion(k, board)
            dp[i][j] = min(dp[i][j], steps)
            jumpTo = board[i][j]
            if jumpTo > 0:
                iJump, jJump = self.idxConversion(jumpTo, board)
                dp[iJump][jJump] = dp[i][j]
                self.updateSquaresBehind(jumpTo, dp, board)
            self.updateSquaresBehind(k, dp, board)
        
        return dp[0][-1]
    
    def updateSquaresBehind(self, squareNo, dp, board):
        n = len(dp)
        i, j = self.idxConversion(squareNo, board)
        initialStep = dp[i][j]
        for p in range(squareNo+1, n*n+1):
            iNext, jNext = self.idxConversion(p, board)
            stepsNext = initialStep + (p - squareNo - 1) // 6 + 1
            if stepsNext > dp[iNext][jNext]:
                break
            else:
                dp[iNext][jNext] = min(dp[iNext][jNext], stepsNext)
            
    def idxConversion(self, squareNo, board):
        i = len(board) - 1 - (squareNo - 1) // len(board)
        j = (squareNo - 1) % len(board) 
        return (i, j)
        """
        

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