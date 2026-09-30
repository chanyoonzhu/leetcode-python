"""
- Array compression
- O(mqn), O(mn)
"""
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        # compress sparse mat2
        M, Q, N = len(mat1), len(mat1[0]), len(mat2[0])
        cols_non_zero_idx = [set() for _ in range(N)]
        cols_index_to_val = [{} for _ in range(N)]
        for r in range(Q):
            for c in range(N):
                if mat2[r][c] != 0:
                    cols_index_to_val[c][r] = mat2[r][c]
                    cols_non_zero_idx[c].add(r)
        
        # compress sparse mat1
        rows_non_zero_idx = [set() for _ in range(M)]
        rows_index_to_val = [{} for _ in range(M)]
        for r in range(M):
            for c in range(Q):
                if mat1[r][c] != 0:
                    rows_index_to_val[r][c] = mat1[r][c]
                    rows_non_zero_idx[r].add(c)

        # calculate    
        res = [[0] * N for _ in range(M)]
        for m in range(M):
            for n in range(N):
                non_zero_indexes = rows_non_zero_idx[m] and cols_non_zero_idx[n] # calculate only when both is non-zero
                for idx in non_zero_indexes:
                    res[m][n] += mat1[m][idx] * mat2[idx][n]
        return res