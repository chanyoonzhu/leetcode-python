"""
- Union find
- intuition: join the water cells from left column to right column, instead of the land cells from top row and bottom row
"""
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
                
        parents, left, right = {}, [list(range(col)) for _ in range(row)], [list(range(col)) for _ in range(row)]
                
        def find(a):
            if a != parents[a]: 
                parents[a] = find(parents[a])
            return parents[a]
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb: parents[pa] = pb
            left[pb[0]][pb[1]] = min(left[pb[0]][pb[1]], left[pa[0]][pa[1]])
            right[pb[0]][pb[1]] = max(right[pb[0]][pb[1]], right[pa[0]][pa[1]])
            
        for i, cell in enumerate(cells):
            x, y = cell
            x, y = x - 1, y - 1
            parents[(x, y)] = (x, y)
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                xx, yy = x + dx, y + dy
                if 0 <= xx < row and 0 <= yy < col and (xx, yy) in parents:
                    union((x, y), (xx, yy))
                    parent = find((x, y))
                    if left[parent[0]][parent[1]] == 0 and right[parent[0]][parent[1]] == col - 1:
                        return i
        return row * col