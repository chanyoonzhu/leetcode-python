class Solution:

    """
    - dfs
    - O(mn), O(mn)
    """
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        def get_next_pos_list(x, y):
            i, j = x, y
            res = []
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x1, y1 = x, y
                while 0 <= x1 + i < n and 0 <= y1 + j < m and maze[x1 + i][y1 + j] == 0:
                    x1 += i
                    y1 += j
                if (x1, y1) not in visited:
                    res.append((x1, y1))
                    visited.add((x1, y1))
            return res
            
        def dfs(begin, end):
            if list(begin) == end:
                return True
            next_pos_list = get_next_pos_list(begin[0], begin[1])
            for next_pos in next_pos_list:
                if dfs(next_pos, end):
                    return True
            return False
         
        n, m = len(maze), len(maze[0])
        visited = set()
        return dfs(start, destination)
    
    """
    - bfs: # todo
    """
        
        