"""
- priority queue
- O(tlogt), O(t)
"""
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(e, p, i) for i, (e, p) in enumerate(tasks)]
        tasks.sort()
        time = task_i = 0
        h = []
        result = []
        while task_i < len(tasks) or h:
            while task_i < len(tasks) and tasks[task_i][0] <= time:
                e, p, i = tasks[task_i]
                heapq.heappush(h, (p, i))
                task_i += 1
            if h:
                p, i = heapq.heappop(h)
                result.append(i)
                time += p
            else:
                time = tasks[task_i][0]     
        return result