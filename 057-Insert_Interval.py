class Solution(object):
    """
    - chronological order
    - O(n), O(n)
    """
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = [newInterval]
        for start, end in intervals:
            if end < newInterval[0]:
                res.insert(len(res)-1, [start, end])
            elif start > newInterval[1]:
                res.append([start,end])
            else:
                res[-1] = [min(res[-1][0], start), max(res[-1][1], end)]
        return res

    """
    - binary search - my solution, better version see: https://leetcode.com/problems/insert-interval/discuss/248611/python-consice-bisect
    - O(logn), O(n)
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def binary_search_larger(nums, target, start, end):
            if start == end:
                return start
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                return binary_search_larger(nums, target, mid + 1, end)
            else:
                return binary_search_larger(nums, target, start, mid)
        
        def binary_search_smaller(nums, target, start, end):
            if start == end:
                return start
            mid = start + (end - start + 1) // 2
            if nums[mid] >= target:
                return binary_search_smaller(nums, target, start, mid-1)
            else:
                return binary_search_smaller(nums, target, mid, end)
        
        results = []
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]
        
        i = binary_search_smaller(starts, newInterval[0], -1, len(starts) - 1)
        j = binary_search_larger(ends, newInterval[1], 0, len(ends))
        
        merged = 0
        if i >= 0 and newInterval[0] <= intervals[i][1]:
            intervals[i][1] = max(intervals[i][1], newInterval[1])
            merged += 1
        if j < len(ends) and newInterval[1] >= intervals[j][0]:
            intervals[j][0] = min(intervals[j][0], newInterval[0])
            merged += 1
            
        results.extend(intervals[:i+1])
        results.extend(intervals[j:])
        
        if merged == 0:
            results.insert(i+1, newInterval)
        elif merged == 2 and results[i][1] >= results[i+1][0]:
            results[i][1] = results[i+1][1]
            del results[i+1]
        
        return results

    """
    - binary search with bisect
    - O(logn), O(n)
    """
    def insert(self, intervals, newInterval):
        i = bisect.bisect_left([i.end for i in intervals], newInterval.start)
        j = bisect.bisect_right([i.start for i in intervals], newInterval.end)-1
        if i <= j:
            newInterval.start = min(newInterval.start, intervals[i].start)
            newInterval.end = max(newInterval.end, intervals[j].end)
        intervals[i: j+1] = [newInterval]
        return intervals
            
s = Solution()
s.insert([[1,3],[6,9]], [2,5])
# s.insert([[0,5],[8,9]], [3,4])