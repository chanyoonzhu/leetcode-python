class MedianFinder(object):
    
    """
    - O(n) for add (O(log(n))binary search + O(n) index shift)
    - O(1) for find median
    
    def __init__(self):
        self.nums = []
        

    def addNum(self, num):
        # insert
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

    def findMedian(self):
        length = len(self.nums)
        if length % 2 == 0:
            return (self.nums[length//2-1] + self.nums[length//2]) / 2.0
        else:
            return self.nums[length//2]
    """
    
    """
    - two heaps
    - O(log(n)) add , O(1) find median
    """

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
            heapq.heappush(self.small, -heapq.heappushpop(self.large,num))
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
        
        
        



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()