"""
- two pointers
- O(n), O(n)
"""
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        
        if len(start) != len(end): return False
        
        start_sequence = [(s, idx) for idx, s in enumerate(start) if s == 'L' or s == 'R']
        end_sequence = [(e, idx) for idx, e in enumerate(end) if e == 'L' or e == 'R']
        if len(start_sequence) != len(end_sequence): return False
        
        for (s, i), (e, j) in zip(start_sequence, end_sequence):
            if s != e: return False # L, R relative sequence must be the same
            if s == 'L': # L can only move to the left
                if i < j:
                    return False
            if s == 'R': # R can only move to the right
                if i > j:
                    return False
            
        return True