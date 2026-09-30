class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        time exceeded, not know why
        r, c = click
        if board[r][c] == 'M':
            board[r][c] == 'X'
            return board
        elif board[r][c] == 'E':
            revealed = set([])
            q = [(r, c)]
            while q:
                rThis, cThis = q.pop()
                revealed.add((r, c))
                adjacentMines = 0
                temp = []
                for i, j in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                    if 0 <= rThis+i < len(board) and 0 <= cThis+j < len(board[0]):
                        if board[rThis+i][cThis+j] == 'M':
                            adjacentMines += 1
                        if (rThis+i,cThis+j) not in revealed:
                            temp.append((rThis+i,cThis+j))
                if not adjacentMines:
                    board[rThis][cThis] = 'B'
                    q.extend(temp)
                else:
                    board[rThis][cThis] = str(adjacentMines)
            return board
        """
        
        
        stack = [(click[0],click[1])]
        visited = set([])
        while stack != []:
            x,y = stack.pop()
            visited.add((x,y))
            if board[x][y] == 'M':
                board[x][y] = 'X'
            else:
                temp = []
                count = 0
                for i,j in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                    if 0<=x+i<len(board) and 0<=y+j<len(board[0]):
                        if board[x+i][y+j]=='M':
                            count += 1
                        if (x+i,y+j) not in visited:
                            temp.append((x+i,y+j))
                if count == 0:
                    board[x][y] = 'B'
                    stack += temp
                else:
                    board[x][y] = str(count)
        return board