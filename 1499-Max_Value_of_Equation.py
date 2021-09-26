"""
- brute force
- O(n^2), O(1)
- TLE
"""
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        result = float("-inf")
        N = len(points)
        for i in range(N):
            xi, yi = points[i]
            for j in range(i + 1, N):
                xj, yj = points[j]
                if xj - xi > k: break
                result = max(result, yi + yj + xj - xi)
        return result

"""
- priority queue
- intuitioin: yi + yj + |xi - xj| where |xi - xj| <= k is same as (yi - xi) + (yj + xj) where |xi - xj| <= k
    heap keeps: ((xi - yi), xi)
- O(nlogk), O(n)
"""
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        h = []
        res = -float('inf')
        for x, y in points:
            while h and h[0][1] < x - k:
                heapq.heappop(h)
            if h:
                res = max(res, -h[0][0] + x + y)
            heapq.heappush(h, (x - y, x))
        return res

"""
- monotonic queue
- O(n), O(n)
"""
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = collections.deque()
        result = float("-inf")
        for j, point in enumerate(points):
            xj, yj = point
            while q and points[q[0]][0] < xj - k:
                q.popleft()
            if q:
                xi, yi = points[q[0]] 
                result = max(result, xj + yj + yi - xi)
            while q and yj - xj >= points[q[-1]][1] - points[q[-1]][0]:
                q.pop()
            q.append(j)
        return result