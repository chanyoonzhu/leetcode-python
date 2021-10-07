class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:

        n = len(stones)
        if (n - 1) % (k - 1): return -1 # n -> n - (k - 1) -> n - 2 *(k - 1) -> ... -> 1
        memo = {}
        prefixes = [0]
        for i in range(n):
            prefixes.append(prefixes[-1] + stones[i])
        
        def dp(l, r):
            if r - l + 1 < k: return 0
            if (l, r) not in memo:
                memo[l, r] = min(dp(l, m) + dp(m + 1, r) for m in range(l, r, k - 1))
                if (r - l) % (k - 1) == 0: #？
                    memo[l, r] += prefixes[r + 1] - prefixes[l] # the cost of combining stones[l:m] and stones[m:r + 1] is always sum(stones[l:r + 1])
            return memo[l, r]