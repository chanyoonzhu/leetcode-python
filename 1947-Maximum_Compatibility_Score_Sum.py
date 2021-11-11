"""
- dynamic programming (with bitmasking)
- O(m* 2^m)
"""
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        
        M, N = len(students), len(students[0])
        scores = [[0] * M for _ in range(M)]
        memo = {}
        
        for i in range(M):
            for j in range(M):
                score = 0
                for k in range(N):
                    if students[i][k] == mentors[j][k]:
                        score += 1
                scores[i][j] = score
        
        @lru_cache(None)
        def dp(i, bit_state):
            if i == M: return 0
            if bit_state not in memo: # can use only bit_state as key, since no bit_state can map to two different i (unlike problem 1066)
                max_score = 0
                for j in range(M):
                    if bit_state & (1<<j): # mentor at bit j is available, can be picked
                        max_score = max(max_score, scores[i][j] + dp(i+1, bit_state ^ (1<<j))) # flip picked mentor's bit to 0
                memo[bit_state] = max_score
            return memo[bit_state]
        
        return dp(0, (1 << M) - 1)