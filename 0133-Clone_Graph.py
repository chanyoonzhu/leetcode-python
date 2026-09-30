"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
clarification:
1. node values unique? yes
2. repeated edges? No
3. self loops? No
4. all nodes connected? Yes
"""
"""
- hashmap + dfs - recursive
- key: use val_to_clone_node map to memoize cloned node
- O(n), O(n)
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        val_to_node = dict()
        return self.dfs(node, val_to_node)
        
    def dfs(self, node, val_to_node):
        if not node:
            return node
        if node.val in val_to_node:
            return val_to_node[node.val]
        val_to_node[node.val] = Node(node.val)
        for nei in node.neighbors:
            val_to_node[node.val].neighbors.append(self.dfs(nei, val_to_node))
        return val_to_node[node.val]

"""
- hashmap + dfs - iterative
- O(n), O(n)
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        val_to_clone = {node.val: Node(node.val)}
        start = node
        stack = [node]
        while stack:
            node = stack.pop()
            for nei in node.neighbors:
                if nei.val not in val_to_clone:
                    stack.append(nei)
                    val_to_clone[nei.val] = Node(nei.val)
                val_to_clone[node.val].neighbors.append(val_to_clone[nei.val])
        return val_to_clone[start.val]

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