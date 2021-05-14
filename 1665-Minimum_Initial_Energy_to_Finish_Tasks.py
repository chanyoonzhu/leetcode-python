"""
- greedy
- intuition: do tasks with bigger gap between actual and minimum first
- caveat: some start with tasks with larger minimum first, which is incorrect: eg.[[1,8],[2,4]] -> 8, not 10
"""
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks_sorted = sorted(tasks, key=lambda x: x[0] - x[1])
        result = remaining = 0
        for actual, minimum in tasks_sorted:
            if minimum >= remaining:
                result += minimum - remaining
                remaining = minimum - actual
            else:
                remaining -= actual
        return result