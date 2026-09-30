"""
- todo: Jarvis Algorithm
- O(m*n). m: number of output 
- todo: has bugs
- https://leetcode.com/problems/erect-the-fence/discuss/103299/Java-Solution-Convex-Hull-Algorithm-Gift-wrapping-aka-Jarvis-march
"""
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
                        
        def crossProductLength(a, b, c):
            return (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0])
        
        def distanceSquare(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        
        result = []
        leftmost_i = 0
        for i in range(1, len(trees)):
            if trees[i][0] < trees[leftmost_i][0]:
                leftmost_i = i
        result.append(trees[leftmost_i])
        
        cur_i = leftmost_i
        while True:
            next_i = 0 # next on fence
            for i in range(1, len(trees)):
                if i == cur_i: continue
                cross = crossProductLength(trees[i], trees[cur_i], trees[next_i])
                if next_i == cur_i or cross >= 0 or (cross == 0 and distanceSquare(trees[i], trees[cur_i]) > distanceSquare(trees[next_i], trees[cur_i])):
                    next_i = i
            for i in range(len(trees)):
                if i == cur_i: continue
                cross = crossProductLength(trees[cur_i], trees[i], trees[next_i])
                if cross == 0:
                    result.append(trees[i])
            cur_i = next_i
            if cur_i == leftmost_i:
                break

        return result