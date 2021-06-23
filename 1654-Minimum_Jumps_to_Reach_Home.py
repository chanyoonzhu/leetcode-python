"""
- bfs
- O(n), O(n)
"""
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q = [(0, 0, False)]
        visited = set((0, False)) # caveat: has to keep two states
        _max = max(x, max(forbidden)) + a + b # caveat: proof?
        forbidden = set(forbidden)
        while q:
            pos, step, isBackward = q.pop(0)
            if pos == x:
                return step
            forward_pos = pos + a
            if forward_pos <= _max and forward_pos not in forbidden and (forward_pos, False) not in visited:
                q.append((forward_pos, step + 1, False))
                visited.add((forward_pos, False))
            if not isBackward:
                backward_pos = pos - b
                if backward_pos >= 0 and backward_pos not in forbidden and (backward_pos, True) not in visited:
                    q.append((backward_pos, step + 1, True))
                    visited.add((backward_pos, True))
        return -1