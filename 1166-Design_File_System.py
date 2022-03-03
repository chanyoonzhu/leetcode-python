"""
- Trie
- O(n)
"""
class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    # O(n), O(n)
    def createPath(self, path: str, value: int) -> bool:
        paths = path[1:].split("/")
        node = self.root
        for path in paths[:-1]:
            if path in node.children:
                node = node.children[path]
            else:
                return False
        if paths[-1] in node.children:
            return False
        else:
            node.children[paths[-1]] = TrieNode(value)
            return True

    # O(n), O(1)
    def get(self, path: str) -> int:
        paths = path[1:].split("/")
        node = self.root
        for path in paths:
            if path in node.children:
                node = node.children[path]
            else:
                return -1
        return node.value if node.value else -1
        

class TrieNode:
    def __init__(self, value=None):
        self.children = defaultdict(set)
        self.value = value
        
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)