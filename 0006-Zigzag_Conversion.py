"""
- array
- O(n), O(n)
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
                
        N = len(s)
        printed_rows = [[] for _ in range(numRows)]
        group_size = max(numRows * 2 - 2, numRows) # edge case: numRows = 1
        for i in range(N): # iterate through s
            c = s[i]
            # calculate which row current character belongs to
            row_idx = i % group_size
            if row_idx >= numRows:
                row_idx = group_size - row_idx
            
            printed_rows[row_idx].append(c)
        return ''.join([''.join(row) for row in printed_rows])