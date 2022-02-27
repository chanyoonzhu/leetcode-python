"""
- n个服务员，m个人等位，给了数组里面元素是每个服务员服务一个人的时间，m>>n，当多个服务员空闲时候，编号最小的去服务，问当你是第m+1个人的时候要等多久
"""
import heapq
from collections import Counter

"""
- O(m)
"""
class Solution:
    def calcWaitTime(self, efficiency: list, customers: int) -> int:
        h = [(time, i) for i, time in enumerate(efficiency)] # end_time, index
        heapq.heapify(h)
        served, cur_time = len(efficiency), 0
        while served < customers:
            end_time, idx = heapq.heappop(h)
            heapq.heappush(h, (end_time + efficiency[idx], idx))
            cur_time = end_time
            served += 1
        return cur_time

import heapq

"""
- O(lcm(efficiency))
"""
class Solution2:
    def calcWaitTime(self, efficiency: list, customers: int) -> int:

        lcm = self.getLcm(efficiency)
        # at time = lcm, completes serving batch_customers
        batch_customers = sum([lcm // time for time in efficiency])
        served = cur_time = 0
        if customers > batch_customers:
            batches = customers // batch_customers
            cur_time += lcm * batches
            served = batch_customers * batches

        h = [(cur_time + time, i) for i, time in enumerate(efficiency)] # end_time, index
        served += len(efficiency)
        heapq.heapify(h)
        while served < customers:
            end_time, idx = heapq.heappop(h)
            heapq.heappush(h, (end_time + efficiency[idx], idx))
            cur_time = end_time
            served += 1
        return cur_time

    def getLcm(self, nums):
        h = [(n, n) for n in nums]
        heapq.heapify(h)
        sieves = Counter()
        while h:
            slot, n = heapq.heappop(h)
            sieves[slot] += 1
            if sieves[slot] == len(nums):
                print(f"lcm = {slot}")
                return slot
            heapq.heappush(h, (slot + n, n))

class Solution3:
    def calcWaitTime(self, efficiency: list, customers: int) -> int:
        lo, hi = 0, min(efficiency) * customers

        def canHandle(t):
            served = len(efficiency) # easy to miss: not 0
            for hours in efficiency:
                served += t // hours
                if served >= customers:
                    return True
            return False

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if canHandle(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

efficiency = [6,7,3,4,1,5]
customers = 100000000
s1 = Solution()
s2 = Solution2()
s3 = Solution3()
# print(s1.calcWaitTime(efficiency, customers))
print(s2.calcWaitTime(efficiency, customers))
print(s3.calcWaitTime(efficiency, customers))


            