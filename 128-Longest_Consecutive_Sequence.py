"""
- set
- O(n), O(n)
- TLE
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        minn, maxx = float("inf"), float("-inf")
        
        for n in nums:
            nums_set.add(n)
            minn = min(minn, n)
            maxx = max(maxx, n)
        
        result = 0
        curr = 0
        i = minn
        while i < maxx + 1:
            while i < maxx + 1 and i in nums_set:
                curr += 1
                i += 1
            result = max(result, curr)
            curr = 0
            i += 1
        
        return result

"""
- union find
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        parents = {n: n for n in nums}
        
        def find(n):
            if parents[n] != n:
                parents[n] = find(parents[n])
            return parents[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 != p2:
                parents[p1] = p2
    
        allNums = set(nums)
        
        for n in nums:
            parents[n] = n
            if n - 1 in allNums:
                union(n, n - 1)
            if n + 1 in allNums:
                union(n + 1, n)
        
        counter = collections.Counter()
        for c, _ in parents.items():
            counter[find(c)] += 1
        return max(counter.values())       