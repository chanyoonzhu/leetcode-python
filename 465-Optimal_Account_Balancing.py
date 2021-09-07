class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balances = collections.defaultdict(int)
        
        for f, t, a in transactions:
            balances[f] -= a
            balances[t] += a
        
        debt = list(balances.values())
        N = len(debt)
        
        def dfs(s):
            nonlocal N
            while (s < N and debt[s] == 0):
                s += 1
            if s == N: return 0
            
            
            r = float('inf')
            for i in range(s + 1, N):
                if debt[i] * debt[s] < 0:
                    # settle s with i
                    debt[i] += debt[s]
                    r = min(r, 1 + dfs(s + 1))
                    # backtrack
                    debt[i] -= debt[s]
            return r
        
        return dfs(0)
