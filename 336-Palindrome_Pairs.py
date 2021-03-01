from collections import defaultdict

class Trie:
    def __init__(self, idx=-1):
        self.children = defaultdict(Trie)
        self.idx = idx
        self.palindroms_below = list() # smart!
    
    def add(self, word, word_idx):
        node = self
        word = word[::-1] # words have to be inserted in reverse
        for i, c in enumerate(word):
            if word[i:] == word[i:][::-1]:
                node.palindroms_below.append(word_idx)
            node = node.children[c]
        node.idx = word_idx
    
    def findPalindromPair(self, word, word_index):
        node = self
        palindrom_pairs = []
        for i, c in enumerate(word):
            if node.idx != -1 and word[i:] == word[i:][::-1]:
                palindrom_pairs.append((word_index, node.idx))
            if c not in node.children:
                return palindrom_pairs
            node = node.children[c]
        if node.idx != -1 and word_index != node.idx:
            palindrom_pairs.append((word_index, node.idx))
        for p in node.palindroms_below:
            if p != word_index:
                palindrom_pairs.append((word_index, p))
        return palindrom_pairs
        
    def is_palindrom(self, word): # in Python, can use word == word[::-1] which is faster
        if len(word) == 1 or len(word) == 0:
            return True
        if word[0] != word[-1]:
            return False 
        return self.is_palindrom(word[1:-1])          

class Solution:
    """
    - Trie
    """
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        result = []
        for i, word in enumerate(words):
            trie.add(word, i)
        for i, word in enumerate(words):
            result.extend(trie.findPalindromPair(word, i))
        return result
        
s = Solution()
ans = s.palindromePairs(["lls","s","sssll"])
print(ans)