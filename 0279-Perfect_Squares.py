"""
- dynamic programming (top-down)
- O(n * sqrt(n)), O(n)
- TLE
"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        
        def dfs(n):
            if dp[n] == float("inf"):
                a = 1
                while a ** 2 <= n:
                    dp[n] = min(dp[n], 1 + dfs(n - a ** 2))
                    a += 1
            return dp[n]
        dfs(n)
        return dp[-1]

"""
- dynamic programming (top-down), optimized with pre-computed squares
- O(n * sqrt(n)), O(n)
- TLE
"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        squares = [i ** 2 for i in range(1, int(sqrt(n))+1)] # optimization: precomputed squares
        
        def dfs(n):
            if dp[n] == float("inf"):
                for square in squares:
                    if n < square: break
                    dp[n] = min(dp[n], 1 + dfs(n - square))
            return dp[n]
        dfs(n)
        return dp[-1]

"""
- dynamic programming (bottom-up), optimized with pre-computed squares
- O(n * sqrt(n)), O(n)
- TLE
"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        squares = [i ** 2 for i in range(1, int(math.sqrt(n))+1)]
        
        for x in range(1, n + 1):
            for s in squares:
                if s > x: break
                dp[x] = min(dp[x], dp[x - s] + 1)
        return dp[-1]

"""
- BFS
"""
class Solution:
    def numSquares(self, n: int) -> int:
        
        # list of square numbers that are less than `n`
        square_nums = [i * i for i in range(1, int(n**0.5)+1)]
        
        q = [(n, 0)]
        visited = set([n])
        while q:
            x, count = q.pop(0)
            if x in square_nums:
                return count + 1
            for sq in square_nums:
                if sq <= x and x - sq not in visited:
                    q.append((x - sq, count + 1))
                    visited.add(x - sq)

"""
- binary search
"""
class Solution:
    def numSquares(self, n: int) -> int:
        
        squares = [i * i for i in range(0, int(n**0.5)+1)]
        
        @lru_cache(None)
        def can_sum_to(x, count):
            if count == 1:
                return x in squares
            for s in squares:
                if s > x: break
                if can_sum_to(x - s, count - 1):
                    return True
            return False
        
        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if can_sum_to(n, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

"""
- todo: mathematics
"""
                    