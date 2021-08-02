"""
- BFS
- O(10 ** 4 + len(deadends)), O(10 ** 4)
"""
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deads = set(deadends)
        if '0000' in deads: return -1 # easy to miss
        visited = set(['0000'])
        q = [('0000', 0)]
        
        def neighbors(x):
            neighbors = [] 
            for i in range(4):
                a = ord(cur[i]) - ord('0')
                for d in (-1, 1):
                    nx = (a + d) % 10
                    neighbors.append(x[:i] + str(nx) + x[i + 1:])
            return neighbors
                    
        while q:
            cur, turns = q.pop(0)
            if cur == target:
                return turns
            for i in range(4):
                for code in neighbors(cur):
                    if code not in deads and code not in visited:
                        visited.add(code)
                        q.append((code, turns + 1))
        return -1