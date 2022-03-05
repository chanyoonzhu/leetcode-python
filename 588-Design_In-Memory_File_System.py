"""
- Trie
"""
class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        
        
    # O(nlog(n))
    def ls(self, path: str) -> List[str]:
        node = self._search(path)
        if node.content != None:
            return [path.split("/")[-1]]
        return sorted([dir_ for dir_ in node.children])

    # O(n)
    def mkdir(self, path: str) -> None:
        self._search(path)
        

    # O(n)
    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._search(filePath)
        if node.content is None:
            node.content = content
        else:
            node.content += content
        
    # O(n)
    def readContentFromFile(self, filePath: str) -> str:
        node = self._search(filePath)
        return node.content
      
    def _search(self, path: str):
        paths = path[1:].split("/")
        node = self.root
        for path in paths:
            if path: # easy to miss
                node = node.children[path]
        return node
        
        
class TrieNode:
    def __init__(self, content=None):
        self.children = defaultdict(TrieNode)
        self.content = content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)