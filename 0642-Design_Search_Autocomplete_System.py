"""
- Trie + heap
"""
class TrieNode:
    def __init__(self):
        self.next = dict()
        self.word = None # stores word at end node to save compute time
        self.rank = 0

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.keyword = ''
        for s, t in zip(sentences, times):
            self._add_sentence(s, t)
            
    def _add_sentence(self, sentence, rank):
        node = self.root
        for ch in sentence:
            if ch not in node.next:
                node.next[ch] = TrieNode()
            node = node.next[ch]
        node.word = sentence
        node.rank -= rank # stores negative of rank to sort by descent order in heap
            
    def input(self, c: str) -> List[str]:
        res = []
        if c != '#':
            self.keyword += c
            res = self._search(self.keyword)
        else:
            self._add_sentence(self.keyword, 1)
            self.keyword = ''
        return [word for _, word in heapq.nsmallest(3, res)]
    
    def _dfs_helper(self, node):
        res = []
        if node:
            if node.word:
                res.append((node.rank, node.word))
            for nextNode in node.next.values():
                res += self._dfs_helper(nextNode)
        return res
    
    def _search(self, sentence):
        node = self.root
        for ch in sentence:
            if ch not in node.next:
                return []
            node = node.next[ch]
        return self._dfs_helper(node)
            
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(["i love you","island","iroman","i love leetcode"],[5,3,2,2])
# print(obj.input('i'))
# print(obj.input(' '))
# print(obj.input('a'))
# print(obj.input('#'))
# print(obj.input('i'))
# print(obj.input(' '))
# print(obj.input('a'))
# print(obj.input('#'))

obj = AutocompleteSystem(["abc","abbc","a"],[3, 3, 3])
print(obj.input('b'))
print(obj.input('c'))
print(obj.input('#'))
print(obj.input('a'))
