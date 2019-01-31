class Solution(object):
    def findNumber(self, arr):
        """
        - O(n) 
        linear search
        """
        

        """
        - O(n) 
        priority queue
        Remember the default heapify is the min heap
        """
        import heapq
        heapq._heapify_max(arr)
        return heapq._heappop_max(arr)

        """
        - O(log(n))
        - binary search
        """

        def findHighest(arr, start, end):
            if start == end:
                return arr[start]
            mid = (start + end) // 2
            if arr[mid] > arr[start] and arr[mid] < arr[end]: # increasing
                return findHighest(arr, mid, end) # highest has to be between mid to end 
            elif arr[mid] < arr[start] and arr[mid] > arr[end]: # decreasing
                return findHighest(arr, start, mid) # highest has to be between start to mid 
            else: # increasing and decreasing
                return max(findHighest(arr, start, mid), findHighest(arr, mid, end)) # highest has to be the larger of either side's highest
                
        findHighest(arr, 0, len(arr))
                

        
        

sl = Solution()
print(sl.findNumber([8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]))
print(sl.findNumber([1, 3, 50, 10, 9, 7, 6]))
print(sl.findNumber([10, 20, 30, 40, 50]))
print(sl.findNumber([120, 100, 80, 20, 0]))
print(sl.findNumber([0, 1, 1, 2, 2, 2, 2, 2, 3, 4, 4, 5, 5, 5, 3, 3, 2, 2, 1, 1]))