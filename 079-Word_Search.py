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
        