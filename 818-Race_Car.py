
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
        return self.dp(target)
        
    @lru_cache(None)
    def dp(self, target):
        steps_forward = target.bit_length() # observation: steps_forward - 1: closest before arriving target; steps_forward - right at or just exceeding target
        instructions = float("inf")
        # case 1: all the way to target using A
        if 2 ** steps_forward - 1 == target:
            instructions = min(instructions, steps_forward)
        else:
            # case 2: A util pass target (stop immediately when past), turn, then A again
            forward_dist = 2 ** steps_forward - 1
            instructions = min(instructions, self.dp(forward_dist - target) + steps_forward + 1) # 1 - for the turn
            # case 3: A as far as possible (but not exceeding target), turn, turn, A to target
            steps_forward -= 1
            forward_dist = 2 ** steps_forward - 1
            for steps_backward in range(steps_forward): 
                backward_dist = 2 ** steps_backward - 1
                instructions = min(instructions, self.racecar(target - (forward_dist - backward_dist)) + steps_forward + 1 + steps_backward + 1) # +1 twice for the two turns
        return instructions