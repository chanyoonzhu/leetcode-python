"""
- bfs with heap
- intuition: push all borders to heap, pop smallest height, add height diff with lower neighbors to results, and recursively push unvisited neighbors to heap
- O(m*nlog(m*n)), O(m*n)
"""
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        M, N = len(heightMap), len(heightMap[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False] * N for _ in range(M)]
        h = []
        
        # Push all on the border into heap
        for i in range(M):
            for j in range(N):
                if i == 0 or i == M - 1 or j == 0 or j == N - 1:
                    visited[i][j] = True
                    heapq.heappush(h, (heightMap[i][j], i, j))
        
        result = 0
        while h:
            height, r, c = heapq.heappop(h)    
            for i, j in DIRECTIONS:
                rr, cc = r + i, c + j
                if 0 <= rr < M and 0 <= cc < N and not visited[rr][cc]:
                    result += max(0, height - heightMap[rr][cc])
                    heapq.heappush(h, (max(heightMap[rr][cc], height), rr, cc)) # caveat: need the max of height and prev_height, not just height
                    visited[rr][cc] = True
        return result