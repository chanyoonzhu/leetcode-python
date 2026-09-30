
class Solution:
    def racecar(self, target: int) -> int:
        
        q = deque([(0, 1, 0)])
        
        while q:
            pos, speed, step = q.popleft()
            if pos == target:
                return step
            # "A"
            q.append((pos + speed, speed * 2, step + 1))
            # "R"
            if pos < 0 and speed > 0:
                continue
            q.append((pos, 1 if speed < 0 else -1, step + 1))

"""
- Dynamic Programming
"""
class Solution:
    def racecar(self, target: int) -> int:
        return self.helper(target)
    
    @lru_cache(None)
    def helper(self, dist):
        if dist == 0:
            return 0
        steps_forward = floor(log(dist + 1, 2)) # easy to miss: +1 (dist is 0 based)
        # case 1. forward until reach
        forward_dist = 2 ** (steps_forward) - 1
        if 2 ** (steps_forward) - 1 == dist:
            return steps_forward

        steps = float("inf")
        # case 2. forward, turn, back, turn, forward
        for steps_backward in range(steps_forward):
            backward_dist = 2 ** steps_backward - 1
            steps = min(steps, steps_forward + steps_backward + self.helper(dist - forward_dist + backward_dist) + 2)
        # case 3. forward (exceed), turn, forward
        steps_forward += 1
        forward_dist = 2 ** (steps_forward) - 1
        steps = min(steps, steps_forward + 1 + self.helper(forward_dist - dist))
        return steps
            
        