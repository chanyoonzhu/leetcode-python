 

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word = False # has to mark eplicitly: app and application can both be legal words
        self.children = {} # hashmap for O(1) search
        

    def insert(self, word):
        
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        curr = self
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


