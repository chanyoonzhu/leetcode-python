class NumArray:

    """
    - cumulative sum
    - update: O(n), sumRange: O(1)
    - time limit exceeded
    """
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.cum_sums = [0]
        for num in self.nums:
            self.cum_sums.append(self.cum_sums[-1] + num)
        

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        for i in range(index, len(self.nums)):
            self.cum_sums[i + 1] += diff
        

    def sumRange(self, left: int, right: int) -> int:
        return self.cum_sums[right + 1] - self.cum_sums[left]

    
"""
- divide and conquer with segment tree
- create: O(n); update: O(logn), O(1); rangesum: O(logn), O(1)
"""
class Node:

    def __init__(self, start, end, total, left=None, right=None):
        self.start = start # subtree index start
        self.end = end # subtree index end
        self.total = total # subtree sum
        self.left = left
        self.right = right

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.root = self.buildRoot(nums, 0, len(nums) - 1)
    
    def buildRoot(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return Node(start, end, nums[start])
        
        mid = start + (end - start) // 2
        left = self.buildRoot(nums, start, mid)
        right = self.buildRoot(nums, mid + 1, end)
        
        return Node(start, end, left.total + right.total, left, right)
        
    def update(self, index: int, val: int) -> None:
        self.updateNodes(self.root, index, val)
        
    def updateNodes(self, node, index, val):
        start, end = node.start, node.end
        if start == end:
            node.total = val
            return
        mid = start + (end - start) // 2
        if mid >= index:
            self.updateNodes(node.left, index, val)
        else:
            self.updateNodes(node.right, index, val)
        node.total = node.left.total + node.right.total   

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeNodes(self.root, left, right)
        
    def sumRangeNodes(self, node, left, right):
        start, end = node.start, node.end
        if start == left and end == right:
            return node.total
        mid = start + (end - start) // 2
        if right <= mid:
            return self.sumRangeNodes(node.left, left, right)
        if left > mid:
            return self.sumRangeNodes(node.right, left, right)
        else:
            return self.sumRangeNodes(node.left, left, mid) + self.sumRangeNodes(node.right, mid + 1, right)

"""
- divide and conquer with binary index tree: https://leetcode.com/problems/range-sum-query-mutable/discuss/75730/148ms-Python-solution-Binary-Indexed-Tree
- create: O(n); update: O(logn), O(1); rangesum: O(logn), O(1)
"""
def __init__(self, nums: list[int]):
    self.n = len(nums)
    self.nums = nums
    self.sums = [0] * (self.n + 1)
    for i in range(self.n):
        k = i + 1
        while k <= self.n:
            self.sums[k] += nums[i]
            k += (k & -k)
    
def update(self, index: int, val: int) -> None:
    k = index + 1
    while k <= self.n:
        self.sums[k] += (val - self.nums[index])
        k += (k & -k)
    self.nums[index] = val

def sumRange(self, left: int, right: int) -> int:
    res, right = 0, right + 1
    while right:
        res += self.sums[right]
        right -= (right & -right)
    while left:
        res -= self.sums[left]
        left -= (left & -left)
    return res

"""
- Range Min Query
"""
class MinNode:
    def __init__(self, min, start, end, left=None, right=None):
        self.min = min
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class NumArray2:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.root = self._buildMinNode(0, len(nums) - 1)

    # O(n)
    def _buildMinNode(self, start, end):
        if start > end:
            return None
        if start == end:
            return MinNode(self.nums[start], start, end)
        mid = start + (end - start) // 2
        l = self._buildMinNode(start, mid)
        r = self._buildMinNode(mid + 1, end)
        return MinNode(min(l.min, r.min), start, end, l, r)
    
    # O(logn)
    def minRange(self, start, end):
        return self._minRangeNode(self.root, start, end)
        
    def _minRangeNode(self, node, start, end):
        n_start, n_end = node.start, node.end
        if n_start == start and n_end == end:
            return node.min
        n_mid = n_start + (n_end - n_start) // 2
        if end <= n_mid:
            return self._minRangeNode(node.left, start, end)
        elif start > n_mid:
            return self._minRangeNode(node.right, start, end)
        else:
            return min(self._minRangeNode(node.left, start, n_mid), self._minRangeNode(node.right, n_mid + 1, end))

s_min = NumArray2([7,2,3,0,5,10,3,12,18])
print(s_min.minRange(4, 5))

        

            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)