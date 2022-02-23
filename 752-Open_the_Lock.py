"""
- BFS
- O(10 ** 4 + len(deadends)), O(10 ** 4)
"""
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        min_turns = 0
        seen = set(deadends)
        if "0000" in deadends: return -1 # easy to miss: "0000" is in deadend
        seen.add("0000")
        digits = [chr(ord_c) for ord_c in range(ord("0"), ord("9") + 1)]
        
        def turn(digit):
            return [digits[(int(digit) + 9) % 10], digits[(int(digit) + 1) % 10]]
        
        q = deque(["0000"])
        while q:
            new_q = deque()
            while q:
                comb = q.popleft()
                if comb == target:
                    return min_turns
                for i in range(4):
                    for next_digit in turn(comb[i]):
                        new_comb = comb[:i] + next_digit + comb[i+1:]
                        if new_comb not in seen:
                            new_q.append(new_comb)
                            seen.add(new_comb)
            min_turns += 1
            q, new_q = new_q, deque()
        return -1