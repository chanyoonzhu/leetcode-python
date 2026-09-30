"""
- binary search (insertion sort)
- O(n) (for array shifting) + O(logn) (for searching) ≈ O(n): addNum.  O(1): findMedian
"""
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)
        """
        # or
        if len(self.nums) == 0:
            self.nums.append(num)
        else:
            l, r = 0, len(self.nums) - 1
            while l < r:
                mid = (l + r) // 2
                if self.nums[mid] == num:
                    l = r = mid
                    break
                elif self.nums[mid] > num:
                    r = mid - 1
                elif self.nums[mid] < num:
                    l = mid + 1
            if num > self.nums[l]:
                self.nums.insert(l+1, num)
            else:
                self.nums.insert(l, num)
        """
        
    def findMedian(self) -> float:
        div, mod = divmod(len(self.nums), 2)
        if mod:
            return self.nums[div]
        return (self.nums[div] + self.nums[div - 1]) / 2.0


    
"""
- two heaps
- O(log(n)) add , O(1) find median
"""
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large = [] # a min heap
        self.small = [] # a max heap
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        import heapq
        if len(self.small) == len(self.large):
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        else:
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        else:
            return -self.small[0]

"""
- follow-ups:
1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?
bucket sort, create an array of bucket of length 101, keep the count of numbers in each bucket, and the count of overall numbers, then it's easy to locate the bucket where the median number resides and find the median by looping through the array-> O(1)
2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
99% of all integer numbers lie in [0,100] means the median is definitely inside [0,100]. Besides the bucket range [0,100] as mentioned above, we just need to keep the count of all numbers, numbers smaller than 0, and numbers larger than 100, and adjust the index of the median element in our buckets of range [0,100].
For example, if we have 100 numbers streamed, and one of the number is smaller than 0, that means the median's index moved forward by 1, we just need to find the 49th element in our buckets in a sorted manner.
"""
        
        
        



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()