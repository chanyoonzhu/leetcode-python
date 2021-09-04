"""
- brute force - my solution
- TLE
"""
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        result = []
        islands = list()
        visited = set()        
        
        for x, y in positions:
            should_join = set()
            for i, island in enumerate(islands):
                for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), ()]:
                    if 0 <= xx < m and 0 <= yy < n and (xx, yy) in island:
                        should_join.add(i)
                        island.add((x, y))
            if not should_join:
                islands.append(set([(x, y)]))
            else:
                joined = set().union(*[island for i, island in enumerate(islands) if i in should_join])
                new_islands = [island for i, island in enumerate(islands) if i not in should_join]
                new_islands.append(joined)
                islands = new_islands
            result.append(len(islands))
        return result

"""
- union find
"""
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        def find(x):
            if x not in parents:
                return x
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            parentX, parentY = find(x), find(y)
            if parentX == parentY:
                return False
            parents[parentX] = parentY
            return True
        
        seen, parents, result, count = set(), {}, [], 0
        for x, y in positions:
            if (x, y) not in seen:
                seen.add((x, y))
                count += 1
                for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if (xx, yy) in seen and union((xx, yy), (x, y)):
                        count -= 1
            result.append(count)
        return result

print(Solution().numIslands2(3,3,[[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]))