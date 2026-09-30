class TicTacToe(object):
    
    """
    - O(n^2)
    
    def __init__(self, n):

        self.grid = [[0]*n for _ in range(n)]
        

    def move(self, row, col, player):

        self.grid[row][col] = player
        if self.isWinner(player):
            return player
        else:
            return 0
    
    def isWinner(self, player):
        
        n = len(self.grid)
        
        for i in range(n):
            j = 0
            while j < n:
                if self.grid[i][j] != player:
                    break
                j += 1
            if j == n: return True
            
        
        for j in range(n):
            i = 0
            while i < n:
                if self.grid[i][j] != player:
                    break
                i += 1
            if i == n: return True
        
        i = 0
        while i < n:
            if self.grid[i][i] != player:
                break
            i += 1
        if i == n: return True
        
        i = 0
        while i < n:
            if self.grid[i][n-i-1] != player:
                break
            i += 1
        if i == n: return True
            
        return False
    """

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diags = [0] * 2
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        point = 1 if player == 1 else -1
        
        self.rows[row] += point
        self.cols[col] += point
        if row == col:
            self.diags[0] += point
        if row == self.n - 1 - col:
            self.diags[1] += point
        
        if point * self.n in [self.rows[row], self.cols[col], self.diags[0], self.diags[1]]:
            return player
        else:
            return 0
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)