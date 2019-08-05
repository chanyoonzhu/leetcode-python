class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        """
        if (len(board) != 3 or len(board[0]) != 3 or 
            len(board[1]) != 3 or len(board[2]) != 3):
            return False
        playsX = self.countPlays(board, 'X')
        playsO = self.countPlays(board, 'O')
        if playsO > playsX or playsX - playsO > 1:
            return False
        hasWonX = self.hasWon(board, 'X')
        hasWonO = self.hasWon(board, 'O')
        if hasWonX and playsX == playsO or hasWonO and playsX == playsO + 1:
            return False
        return True
        
    def hasWon(self, board: List[str], player: str) -> bool:
        BOARD_SIZE = 3
        for i in range(BOARD_SIZE):
            if board[i] == player * BOARD_SIZE:
                return True
            if (board[0][i] == player and 
                board[0][i] == board[1][i] == board[2][i]):
                return True
        if (board[1][1] == player and
            (board[0][0] == board[1][1] == board[2][2] or
             board[0][2] == board[1][1] == board[2][0])):
            return True
        return False
    
    def countPlays(self, board: List[str], player: str) -> int:
        BOARD_SIZE = 3
        total = 0
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == player:
                    total += 1
        return total
        """
        
        SIZE = 3
        turns = 0
        rows, cols  = [0] * SIZE, [0] * SIZE
        diag1 = diag2 = 0
        for i in range(SIZE):
            for j in range(SIZE):
                if board[i][j] == 'X':
                    turns += 1
                    rows[i] += 1
                    cols[j] += 1
                    if i == j:
                        diag1 += 1
                    if i + j == SIZE - 1:
                        diag2 += 1
                elif board[i][j] == 'O':
                    turns -= 1
                    rows[i] -= 1
                    cols[j] -= 1
                    if i == j:
                        diag1 -= 1
                    if i + j == SIZE - 1:
                        diag2 -= 1
        
        wonX = (3 in rows) or (3 in cols) or diag1 == 3 or diag2 == 3
        wonO = (-3 in rows) or (-3 in cols) or diag1 == -3 or diag2 == -3
        
        if turns == 0 and not wonX or turns == 1 and not wonO:
            return True
        return False
    
        