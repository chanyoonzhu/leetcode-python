"""
- brute force with prefix sum
- O(n^2), O(n)
"""
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        
        diffs_prefix = [0] # stores the diffs of counts of 1 and 0 uptil each index i
        for x in nums:
            diffs_prefix.append(diffs_prefix[-1] + (1 if x == 1 else -1))
        
        res = 0
        N = len(diffs_prefix)
        for i in range(N):
            for j in range(i):
                if diffs_prefix[i] - diffs_prefix[j] > 0:
                    res += 1
        return res

"""
- segment tree
- O(nlogn)
"""


class Node:
    def __init__(self, start, end, total, left=None, right=None):
        self.start = start # diff_prefix start
        self.end = end # diff_prefix end
        self.total = total # total count from start to end
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self):
        self.root = Node(-10**5, 10**5, 0)
        self.mod = 10 ** 9 + 7

    def update(self, val):
        self.updateNode(self.root, val)

    def updateNode(self, node, val):
        node.total = (node.total + 1) % self.mod
        if node.start != node.end:
            mid = node.start + (node.end - node.start) // 2
            if val <= mid:
                if not node.left:
                    node.left = Node(node.start, mid, 0)
                self.updateNode(node.left, val)
            else:
                if not node.right:
                    node.right = Node(mid+1, node.end, 0)
                self.updateNode(node.right, val)
    
    def sumRange(self, start, end):
        return self.sumRangeNode(self.root, start, end)

    def sumRangeNode(self, node, start, end):
        if node.start == start and node.end == end:
            return node.total
        mid = node.start + (node.end - node.start) // 2
        if end <= mid:
            return self.sumRangeNode(node.left, start, end) if node.left else 0
        elif start > mid:
            return self.sumRangeNode(node.right, start, end) if node.right else 0
        else:
            total = 0
            if node.left: total = (total + self.sumRangeNode(node.left, start, mid)) % self.mod
            if node.right: total = (total + self.sumRangeNode(node.right, mid+1, end)) % self.mod
            return total

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: list[int]) -> int:
        
        res = 0
        tree = SegmentTree()
        # stores the accumulated diff of counts of 1 and 0 uptil each index i eg:[0,1,1,0,1] => [0, -1, 0, 1, 0, 1]
        # problem becomes: find the total count of all previous diff_prefixes that is less than current diff_prefix
        diffs_prefix = [0] 
        tree.update(0) # diff_prefix 0 should have count 1
        for x in nums:
            diffs_prefix.append(diffs_prefix[-1] + (1 if x == 1 else -1))
            tree.update(diffs_prefix[-1])
            res += tree.sumRange(-10**5, diffs_prefix[-1] - 1) ## find total number diff prefixes that is less than diffs_prefix[-1]
        return res % (10 ** 9 + 7)

"""
- prefix-sum + Hashmap
- O(n)
"""
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        res = 0
        # pre - prev diff_prefix
        # cur - current diff_prefix
        # cnt - counts of diff_prefixes
        # precnt - total count of diff_prefix <= cur
        pre, precnt, mod = 0, 0, int(10**9+7)
        cnt = Counter({0: 1})
        for x in nums:
            cur = pre + (1 if x == 1 else -1)
            # if prefix[i] = prefix[i-1] + 1: current number of qualified sequences are previous sum of count of prefixes 
            # that < prefix[i-1] (which is precnt) + count of prefix[i-1]
            if cur == pre + 1:
                precnt += cnt[pre] % mod
            # if prefix[i] = prefix[i-1] - 1: current number of qualified sequences are previous sum of count of prefixes 
            # that < prefix[i-1] (which is precnt) - count of prefix[i-1]
            else:  # cur == pre - 1
                precnt -= cnt[pre-1] % mod
            res += precnt
            cnt[cur] += 1
            pre = cur
            
        return res % mod