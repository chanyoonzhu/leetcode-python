from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        res = []

        heap = [(-val, key) for key, val in counts.items()]
        heapq.heapify(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


"""
- quick sort
- O(n), O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counts = [(v, k) for k, v in counter.items()]
        l, r = 0, len(counts) - 1
        self.quickSort(counts, l, r, k)
        return [x for _, x in counts[:k]]
        
    def quickSort(self, counts, l, r, k):
        while l <= r:
            idx = self.partition(counts, l, r)
            if idx == k - 1:
                return
            elif idx < k - 1:
                l = idx + 1
            else:
                r = idx - 1

    def partition(self, nums, start, end):
        pivot = nums[end][0]
        idx = start
        for i in range(start, end):
            if nums[i][0] >= pivot:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        nums[idx], nums[end] = nums[end], nums[idx]
        return idx