"""
- priority queue
- O(nlogn), O(n)
"""
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        result = []
        q_free = [[weight, i, 0] for i, weight in enumerate(servers)]
        q_taken = []
        heapq.heapify(q_free)
        time = 0
        for j, task in enumerate(tasks):
            while q_taken and q_taken[0][0] <= j or not q_free:
                time, weight, i = heapq.heappop(q_taken)
                heapq.heappush(q_free, [weight, i, time])
            weight, i, time = heapq.heappop(q_free)
            result.append(i)
            heapq.heappush(q_taken, [max(time, j) + task, weight, i])
        return result