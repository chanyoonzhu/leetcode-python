"""
- dfs
- O(mn), O(mn)
"""
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        self.n, self.s, self.e, self.w = x, x, y, y
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        visited = set()
        
        def dfs(r, c):
            if r < self.n: self.n = r
            if r > self.s: self.s = r
            if c < self.w: self.w = c
            if c > self.e: self.e = c
            visited.add((r, c))
            for i, j in DIR:
                nr, nc = r + i, c + j
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == "1" and (nr, nc) not in visited:
                    dfs(nr, nc)
                    
        dfs(x, y)
        print(self.n, self.s, self.e, self.w)
        return (self.s - self.n + 1) * (self.e - self.w + 1)

"""
- binary search
- O(mlogn + nlogm), O(1)
"""
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        n, s, w, e = x, x, y, y
        n = self.getLowerBoundary(self.rowHasOne, image, 0, n)
        s = self.getUpperBoundary(self.rowHasOne, image, s, len(image) - 1)
        w = self.getLowerBoundary(self.colHasOne, image, 0, w)
        e = self.getUpperBoundary(self.colHasOne, image, e, len(image[0]) - 1)
        return (s - n + 1) * (e - w + 1)
        
    def getLowerBoundary(self, row_or_col_func, image, lo, hi):
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if row_or_col_func(image, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    def getUpperBoundary(self, row_or_col_func, image, lo, hi):
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if row_or_col_func(image, mid):
                lo = mid
            else:
                hi = mid - 1
        return lo   
        
    
    def rowHasOne(self, image, r):
        return any(cell == "1" for cell in image[r])
    
    def colHasOne(self, image, c):
        return any(image[r][c] == "1" for r in range(len(image)))
        