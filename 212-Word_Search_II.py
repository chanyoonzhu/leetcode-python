import collections

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        """
        - dfs
        - time limit exceeded - has to go through each word one by one
        - store positions of a char as set in a hashmap
        - dfs for each letter in word
        
        table = collections.defaultdict(set)
        res = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                table[board[i][j]].add((i,j))  
        for word in words:
            if len(word) == 0:
                res.add(word)
            else:
                c = word[0]
                for (i, j) in table[c]:
                    visited = set()
                    visited.add((i,j))
                    if self.dfs(board, word[1:], table, i, j, visited):
                        res.add(word)
        
        return list(res)
            
    def dfs(self, board, s, table, i, j, visited):
        if not s:
            return True
        c = s[0]
        for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            visitedCopy = visited.copy()
            if (x,y) in table[c] and (x, y) not in visitedCopy:
                visitedCopy.add((x, y))
                if self.dfs(board, s[1:], table, x, y, visitedCopy):
                    return True
        return False
        """
        
        """
        - Trie and dfs
        - does not need to goe through each word
        """
        res = []
        
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False # words can have duplicates!
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.children:
            return
        tmp = board[i][j]
        board[i][j] = '#'
        self.dfs(board, node.children[tmp], i+1, j, path+tmp, res)
        self.dfs(board, node.children[tmp], i-1, j, path+tmp, res)
        self.dfs(board, node.children[tmp], i, j+1, path+tmp, res)
        self.dfs(board, node.children[tmp], i, j-1, path+tmp, res)
        board[i][j] = tmp
        
                
        
class TrieNode(object):
    
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie(object):
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isWord
        

print(Solution().findWords([["a","a"]],
["aaa"]))