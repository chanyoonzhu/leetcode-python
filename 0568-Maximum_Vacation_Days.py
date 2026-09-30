"""
- Dynamic programming (top-down)
- O(kn^2), O(kn)
"""
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        
        N = len(flights)
        k = len(days[0])
        
        graph = defaultdict(set)
        for r in range(N):
            for c in range(N):
                if flights[r][c] == 1:
                    graph[r].add(c)
                 
        @lru_cache(None)
        def dp(city, week):
            if week == k:
                return 0
            holiday = 0
            for next_c in (graph[city] | set([city])): # easy to miss: can choose to stay
                holiday = max(holiday, days[next_c][week] + dp(next_c, week + 1))
            return holiday
        
    
        return dp(0, 0)