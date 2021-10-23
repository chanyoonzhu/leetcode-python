"""
- Trie (2 tries) + hashmap
"""
class TrieNode:
    
    def __init__(self):
        self.next = {}
        self.index = -1

class WordFilter:

    def __init__(self, words: List[str]):
        self.pref_root = TrieNode() # prefix Trie
        self.suf_root = TrieNode() # suffix Trie
        self.memo = {} # memoize prev search result
        for i, word in enumerate(words):
            self._addWord(self.pref_root, word, i)
            self._addWord(self.suf_root, word[::-1], i)   
    
    def _addWord(self, root, word, index):
        node = root
        for c in word:
            if c not in node.next:
                node.next[c] = TrieNode()
            node = node.next[c]
            node.index = index

    def f(self, prefix: str, suffix: str) -> int:
        if (prefix, suffix) in self.memo: return self.memo[(prefix, suffix)]
        prefixes = sorted(self._search(self.pref_root, prefix), reverse=True)
        suffixes = set(self._search(self.suf_root, suffix[::-1]))
        for idx in prefixes:
            if idx in suffixes:
                self.memo[(prefix, suffix)] = idx
                return idx
        return -1  
            
    def _search(self, root, prefix):
        node = root
        for c in prefix:
            if c not in node.next:
                return []
            node = node.next[c]
        return self._dfs(node)
        
    def _dfs(self, node):
        output = []
        if node:
            if node.index != -1:
                output.append(node.index)
            for c in node.next:
                output.extend(self._dfs(node.next[c]))
        return output