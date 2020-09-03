"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    """
    - dfs
    - O(n), O(n)
    """
    
    def __init__(self):
        self.visited = dict()  # declaring as global to prevent defining a nested dfs() method in cloneGraph
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: # easy to miss for [[]]
            return node
        if node.val in self.visited:
            return self.visited[node.val]
        copy = Node(node.val)
        self.visited[node.val] = copy # or self.visited[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(self.cloneGraph(neighbor))
        return copy

    """
    - bfs: harder
    - O(n), O(n)
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = dict()
        queue = [node]
        visited[node] = Node(node.val)
        
        while queue:
            current = queue.pop(0)
            for neighbor in current.neighbors:
                if neighbor not in visited: # create non-exist neighbor 
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[current].neighbors.append(visited[neighbor]) # add neighbor
        
        return visited[node]