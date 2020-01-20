class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        """
        time limit exceeded 
        """
        m, n = len(mat), len(mat[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                val = mat[i][j]
                for ki in range(-K, K+1):
                    for kj in range(-K, K+1):
                        if i+ki >= 0 and i+ki < m and j+kj >= 0 and j+kj < n:
                            res[i+ki][j+kj] += val
        return res

        """
        -O(m*n), O(m*n)
        -dp, range sum
        - https://leetcode.com/problems/matrix-block-sum/discuss/477036/JavaPython-3-PrefixRange-sum-w-analysis-similar-to-LC-30478
        in line, 37, i - K or j - K is actually i - K - 1 + 1 and j - K - 1 + 1
        """
        m, n = len(mat), len(mat[0])
        res = [[0] * n for _ in range(m)]
        rangeSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                rangeSum[i+1][j+1] = rangeSum[i+1][j] + rangeSum[i][j+1] - rangeSum[i][j] + mat[i][j]
        for i in range(m):
            for j in range(n):
                r1, r2, c1, c2 = max(0, i - K), min(m, i + K + 1), max(0, j - K), min(n, j + K + 1)
                res[i][j] = rangeSum[r2][c2] - rangeSum[r1][c2] - rangeSum[r2][c1] + rangeSum[r1][c1]
        return res