"""
- brute force
- O(n^2), O(n)
"""
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        N = len(cars)
        result = [float("inf")] * N
        for i in range(N):
            pos_i, v_i = cars[i]
            for j in range(i + 1, N):
                pos_j, v_j = cars[j]
                if v_i > v_j:
                    result[i] = min(result[i], (pos_j - pos_i + 0.0) / (v_i - v_j))
        return [-1 if a == float("inf") else a for a in result]

"""
- mononistically decreasing stack
- O(n^2), O(n)
"""
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        result = []
        stack = [] # cars that can collide with current car, collision time decreasing
        for position, v in cars[::-1]:
            while stack and (v <= stack[-1][1] or (stack[-1][0] - position) / (v - stack[-1][1]) >= stack[-1][2]):
                stack.pop()
            if not stack:
                stack.append((position, v, float("inf")))
                result.append(-1)
            else:
                collideTime = (stack[-1][0] - position) / (v - stack[-1][1])
                stack.append((position, v, collideTime))
                result.append(collideTime)
        return result[::-1]