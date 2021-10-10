"""
- dynamic programming
- intuition: divide into subarrays of max size k (shelfWidth), minimize the sum of the largest value in each subarray
- O(n^2), O(n)
"""
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        N = len(books)
        prefix_width = [0] * (N + 1)
        for i in range(1, N + 1):
            prefix_width[i] = prefix_width[i - 1] + books[i - 1][0]
        
        dp = [0] + [float("inf")] * N
        for i in range(1, N + 1):
            for j in range(i - 1, -1, -1): # j is the last book in previous row
                if (prefix_width[i] - prefix_width[j] <= shelfWidth):
                    dp[i] = min(dp[i], dp[j] + max([h for _, h in books[j: i]]))
                else:
                    break
        
        return dp[-1]