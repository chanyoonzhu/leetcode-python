import collections

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        table = collections.defaultdict(list)
        
        l = r = 0
        n = len(tree)
        maxNum = 0
        
        while r < n:
            table[tree[r]].append(r)
            if len(table) > 2:
                while len(table) > 2 and l < r:
                    del table[tree[l]][0]
                    if len(table[tree[l]]) == 0:
                        del table[tree[l]]
                    l += 1
            maxNum = max(maxNum, r-l+1)
            r += 1     
                              
        return maxNum

print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))