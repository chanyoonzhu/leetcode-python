import collections

class Solution:
    """
    - sliding window
    - O(n), O(1)
    """
    def totalFruit(self, tree: List[int]) -> int:
        counts = collections.Counter()
        i = result = 0
        for j, _type in enumerate(tree):
            counts[_type] += 1
            while len(counts) > 2:
                counts[tree[i]] -= 1
                if counts[tree[i]] == 0:
                    del counts[tree[i]]
                i += 1
            result = max(result, j - i + 1)
        return result

print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))