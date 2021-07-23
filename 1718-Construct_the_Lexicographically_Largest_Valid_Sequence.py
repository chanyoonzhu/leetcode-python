"""
- backtracking + greedy
- ?
"""
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        N = (n - 1) * 2 + 1
        result = [0] * N
        used = set()
        
        
        def backtrack(idx):
            if idx == N:
                return True if len(used) == n else False
            if result[idx]: # current pos taken
                return backtrack(idx + 1)
            for x in range(n, 0, -1):
                if x not in used:
                    idx2 = idx + x if x != 1 else idx
                    if idx2 < N and result[idx2] == 0:
                        result[idx], result[idx2] = x, x
                        used.add(x)
                        if backtrack(idx + 1):
                            return True
                        result[idx], result[idx2] = 0, 0
                        used.remove(x)
            return False
        
        backtrack(0)
                    
        return result