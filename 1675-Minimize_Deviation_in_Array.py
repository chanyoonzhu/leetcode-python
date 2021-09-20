"""
- priority queue
- intuition:  heap = [reduced_num, num_upper_limit]
    1. can change both odd/even number, eliminate one change by reducing all even number to odd
    2. while at the same time keep track of the largest that number can be
    3. keep a running maxx, the deviation candidate is the maxx - the head of the heap
    4. push the popped * 2 (while in limit) to the heap to consider next
"""
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            tmp = num
            while not tmp % 2 and tmp:
                tmp //= 2
            heapq.heappush(heap, (tmp, num if tmp != num else tmp * 2)) # even limit is original, odd limit is num * 2 (num * 2 will be divided by 2 next time since its even)
        
        maxx = max([n for n, _ in heap])
        result = float("inf")
        
        while len(heap) == len(nums):
            num, limit = heapq.heappop(heap)
            result = min(result, maxx - num)
            if num < limit:
                heapq.heappush(heap, (num * 2, limit)) # push next candidate
                maxx = max(maxx, num * 2) # update running maxx
        return result