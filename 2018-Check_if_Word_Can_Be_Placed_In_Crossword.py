"""
- 2 pointers
- find each horizontal/vertical strip using two pointers, see if there could be a match
- O(mn), O(mn)
"""
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
        M, N = len(board), len(board[0])
        word_len = len(word)
        
        for i in range(M):
            l = 0
            while l < N:
                if board[i][l] == "#":
                    l += 1
                else:
                    r = l
                    while r < N and board[i][r] != "#":
                        r += 1
                    if r - l == word_len:
                        hori_strip = ''.join(board[i][l:r])
                        if self.isMatch(hori_strip, word):
                            return True 
                    l = r + 1
        for j in range(N):
            l = 0
            while l < M:
                if board[l][j] == "#":
                    l += 1
                else:
                    r = l
                    while r < M and board[r][j] != "#":
                        r += 1
                    if r - l == word_len:
                        vertical_strip = ''.join([board[k][j] for k in range(l, r)])
                        if self.isMatch(vertical_strip, word):
                            return True          
                    l = r + 1
            
        return False
    
    def isMatch(self, pattern, word): # easy to miss: can match both original and reversed
        return self.isMatchInOrder(pattern, word) or self.isMatchInOrder(pattern, word[::-1])
            
        
    def isMatchInOrder(self, pattern, word):
        if len(pattern) != len(word):
            return False
        for i in range(len(pattern)):
            if pattern[i] == " ":
                continue
            if pattern[i] != word[i]:
                return False
        return True