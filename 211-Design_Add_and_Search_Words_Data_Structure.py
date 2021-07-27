"""
- Trie
- addWord: O(M), O(M); searchWord: time - O(M) best case, O(26^M) worst case M - length of the word; space - O(1) best case, O(M) worst case for recursion stack
"""
class TrieNode:
    def __init__(self):
        self.isWord = False # mark word end
        self.children = collections.defaultdict(TrieNode)

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True 

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
    
    def dfs(self, node, word, i):
        if i == len(word):
            return True if node.isWord else False
        cur = node
        c = word[i]
        if c == ".":
            for child in cur.children:
                if self.dfs(cur.children[child], word, i + 1):
                    return True
        elif c in cur.children:
            return self.dfs(cur.children[c], word, i + 1)
        else:
            return False 
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)