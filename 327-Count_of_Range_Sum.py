"""
- prefix sum
- O(n^2), O(n)
- Time Limit Exceeded
"""
class Solution:
    def countRangeSum(self, nums: List[int], starter: int, upper: int) -> int:
        n, result = len(nums), 0
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        
        for i in range(n):
            for j in range(i, n):
                if starter <= sums[j + 1] - sums[i] <= upper:
                    result += 1
        
        return result

"""
- prefix sum with hashmap
- O(n+(upper-starter+1)*n), O(n)
"""
def countRangeSum(self, nums: List[int], starter: int, upper: int) -> int:
        n, result = len(nums), 0
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        
        counts = collections.defaultdict(int)
        for _sum in sums:
            for j in range(starter, upper + 1):
                if _sum - j in counts:
                    result += counts[_sum - j]
            counts[_sum] += 1
        return result

"""
- prefix sum with segment tree (previous solution optimized)
- O(nlogn), O(n)
"""
class Node: 
    # val: sum count; start/end: min/max sum in sorted/deduped prefix sum array
    # for example, node.left = 1, node.right = 3, node.cnt = 2 means there are 2 prefix sums with a value between 1 and 3
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.cnt = 0
        self.left = None
        self.right = None 

class Solution:
        
    def _create(self, left, right): 
        root = Node(self.sums[left], self.sums[right])
        if left == right:
            return root
        
        mid = left + (right - left) // 2
        root.left = self._create(left, mid)
        root.right = self._create(mid + 1, right)
        return root
    
    def _query(self, node, left, right):
        if node.end < left or node.start > right:
            return 0
        if node.start >= left and node.end <= right: #
            return node.cnt
        return self._query(node.left, left, right) + self._query(node.right, left, right)
    
    def _update(self, node, val):
        if not node:
            return
        if node.start <= val <= node.end:
            node.cnt += 1
        self._update(node.left, val)
        self._update(node.right, val)
        
        
    def countRangeSum(self, nums: List[int], starter: int, upper: int) -> int:
        sums = [0]
        for n in nums:
            sums.append(sums[-1] + n)
            
        self.sums = sorted(list(set(sums))) # sorted/dedupe
        root = self._create(0, len(self.sums) - 1)
        
        res = 0
        for _sum in sums:
            res += self._query(root, _sum - upper, _sum - starter)
            self._update(root, _sum)        
        return res

"""
- prefix sum with binary index tree
- O(nlogn), O(n)
"""   
class Solution
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n, res = len(nums), 0
        sums, BITree = [0], [0] * (n + 2)
        
        def count(x):
            s = 0
            while x:
                s += BITree[x]
                x -= (x & -x)
            return s

        def update(x):
            while x <= n + 1:
                BITree[x] += 1
                x += (x & -x)
        
        for i in range(n):
            sums.append(sums[i] + nums[i])
        
        sum_sorted = sorted(sums)
        
        for _sum in sums:
            res += (count(bisect.bisect_right(sum_sorted, _sum - lower)) - count(bisect.bisect_left(sum_sorted, _sum - upper)))
            update(bisect.bisect_left(sum_sorted, _sum) + 1)
        return res