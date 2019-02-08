import heapq

class TrieNode(object):
    
    def __init__(self):
    
        self.occurrences = 0 
        self.data = "" # stores input sentence as string
        self.children = {}

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        
        self.trie = TrieNode()
        self.currSearch = self.trie # for search based on previous result
        self.noMatch = False # for search based on previous result
        self.matchedStr = "" # for add sentence based on previous result
        self.outStr = "" # for add sentence based on previous result
        
        for i, sentence in enumerate(sentences):
            occurrences = times[i]
            self.addSentence(self.trie, sentence, occurrences)
    
    def addSentence(self, root, sentence, n):
        
        curr = root
        for c in sentence:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.occurrences += n
        curr.data = (self.matchedStr + sentence)

        
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        heap, res = [], []
        
        if c != '#':
            # search
            if self.noMatch or c not in self.currSearch.children:
                self.noMatch = True
                self.outStr += c
                return []
            else:
                self.matchedStr += c
                self.currSearch = self.currSearch.children[c]
                self.dfs(self.currSearch, heap)        
                        
        else:
            # add sentence, clear input and currSearch
            self.addSentence(self.currSearch, self.outStr, 1)
            self.currSearch = self.trie
            self.noMatch = False
            self.outStr = ""
            self.matchedStr = ""
            return []
        
        for _ in range(min(len(heap), 3)):
            res.append(heapq.heappop(heap)[1])
        
        return res
            
            
    
    def dfs(self, node, heap):
        if node.data:
            heapq.heappush(heap, (-node.occurrences, node.data))
        for char, node in node.children.items(): # mistake: don't use else! search results can have tails that make them other results!
            self.dfs(node, heap)
        


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
