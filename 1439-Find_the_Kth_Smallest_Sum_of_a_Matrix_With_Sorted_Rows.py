"""
- priority queue
- Similar: 373-Find K Pairs with Smallest Sums
- O(k * logk * (m-1)
"""
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        M, N = len(mat), len(mat[0])
        heap = [(sum([row[0] for row in mat]), tuple([0] * M))]
        result = heap[0][0]
        visited = set(tuple([0] * M))
        
        nth = 1
        while nth <= k and heap:
            sum_, indexes = heapq.heappop(heap)
            if nth == k: return sum_
            indexes = list(indexes)
            for i in range(M):
                if indexes[i] < len(mat[i]) - 1:
                    indexes[i] += 1
                    if tuple(indexes) not in visited:
                        heapq.heappush(heap, (sum_ - mat[i][indexes[i] - 1] + mat[i][indexes[i]], tuple(indexes)))
                        visited.add(tuple(indexes))
                    indexes[i] -= 1 # backtrack
            nth += 1