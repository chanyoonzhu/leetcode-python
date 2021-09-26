"""
- union find
"""
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N, result = len(arr), -1
        parents, one_counts = {}, [0] * (N + 1) # one_counts stores number of adjacent 1s

        def find(x):
            parents.setdefault(x, x)
            if parents[x] != x: 
                parents[x] = find(parents[x])
            return parents[x]
		
        def union(x, y):
            one_counts[find(y)] += one_counts[find(x)] # smart!
            parents[find(x)] = find(y)
        
        if m == N: return N
        for i, a in enumerate(arr):
            one_counts[a] = 1
            for b in [a - 1, a + 1]:
                if 1 <= b <= N and one_counts[b]:
                    if one_counts[find(b)] == m: result = i
                    union(a, b)
        return result

"""
- array
- O(n), O(n)
"""
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr): return m
        length, ans = [0] * (len(arr) + 2), -1
        for i, a in enumerate(arr):
            left, right = length[a - 1], length[a + 1]
            if left == m or right == m: ans = i
            length[a - left] = length[a + right] = left + right + 1
        return ans