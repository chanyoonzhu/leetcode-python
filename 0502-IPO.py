"""
- greedy with priority queue
- O(klogt), O(t)
"""
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        tasks = list(zip(capital, profits))
        tasks.sort()
        
        capital = w
        task_i = 0
        h = [] # tasks that we have enough capital to start at each step
        for _ in range(k):
            while task_i < len(tasks) and capital >= tasks[task_i][0]:
                c, p = tasks[task_i]
                heapq.heappush(h, -p)
                task_i += 1
            if h:
                capital += -heapq.heappop(h) # greedy complete the task that has highest profit
        return capital