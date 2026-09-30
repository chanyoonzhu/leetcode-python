"""
- Dijkstra (BFS + priority queue)
- TLE
"""
class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        
        def find_smallest_path(paths, i, prev_i, cost):
            new_path = [cost, paths[prev_i][1] + [i]]
            if i not in paths:
                return new_path
            existing_cost = paths[i][0]
            if existing_cost < cost: 
                return paths[i]
            elif existing_cost > cost:
                return current_path
            i1 = i2 = 0
            existing_path, current_path = paths[i][1], new_path[1]
            while i1 < len(existing_path) and i2 < len(current_path):
                if existing_path[i1] > current_path[i2]:
                    return new_path
                elif existing_path[i1] < current_path[i2]:
                    return paths[i]
                else:
                    i1 += 1
                    i2 += 1
            if i1 < len(existing_path): return new_path
            if i2 < len(current_path): return paths[i]
            return paths[i]

        N = len(coins)
        paths = {1: [coins[0], [1]]} # index, [cost, coin_path]
        
        
        h = [(coins[0], 1, 1)] # cost, index, prev_index
        result = []
        min_cost = float("inf")
               
        while h:
            cost, i, prev_i = heapq.heappop(h)
            paths[i] = find_smallest_path(paths, i, prev_i, cost)
            if cost > min_cost: break
            if i == N:
                min_cost = cost
                result = paths[i][1]
            for k in range(1, min(maxJump + 1, N + 1 - i)):
                next_i = i + k
                if coins[next_i-1] != -1 and next_i not in paths:
                    heapq.heappush(h, (cost + coins[next_i-1], next_i, i))
        return result

"""
- monotonic decreasing queue
- O(n), O(n)
"""
class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        
        if coins[-1] == -1: return []
        N = len(coins)
        dp = [None] * N
        dp[-1] = (coins[-1], N) # cost at i, to
        window = collections.deque() # monotonically decreasing queue
        window.append((coins[-1], N - 1)) # total cost, next i
        
        i = len(coins) - 2
        while i >= 0:
            if not window: break
            if coins[i] != -1:
                cost = coins[i] + window[-1][0] # window[-1][0] is the min cost i can reach within maxJump
                to = window[-1][1]
                dp[i] = (cost, to)
                while window and window[0][0] >= cost: # key: = is necessary to replace with smaller i to guarantee lexicographically order
                    window.popleft()
                window.appendleft((cost, i))
            if i + maxJump == window[-1][1]: # out of maxJump boundary, pop out
                window.pop()
            i -= 1
        if not dp[0]:
            return []
        i = 0
        result = []
        while i != len(coins):
            result.append(i + 1)
            i = dp[i][1]
        return result