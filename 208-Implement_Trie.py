 
"""
- Trie with two classes
"""
class TrieNode(object):
    
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: 'str') -> 'None':
        """
        Inserts a word into the trie.
        """
        pointer = self.root
        for c in word:
            if c not in pointer.children:
                pointer.children[c] = TrieNode()
            pointer = pointer.children[c]
        pointer.isWord = True  
        

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the trie.
        """
        pointer = self.root
        for c in word:
            if c not in pointer.children:
                return False
            else:
                pointer = pointer.children[c]
        return pointer.isWord == True
        

    def startsWith(self, prefix: 'str') -> 'bool':
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pointer = self.root
        for c in prefix:
            if c not in pointer.children:
                return False
            else:
                pointer = pointer.children[c]
        return True


"""
- Trie with only one class
"""
from collections import defaultdict

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = defaultdict(Trie)
        self.end = False
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self
        for c in word:
            trie = trie.children[c]
        trie.end = True
                
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self
        for c in word:
            if c not in trie.children:
                return False
            trie = trie.children[c]
        return trie.end == True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self
        for c in prefix:
            if c not in trie.children:
                return False
            trie = trie.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


