"""
- greedy + knapsack dp
- O(n*t), O(n*t)
"""
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1]) # greedily take course ends earlier
        
        @lru_cache(None)
        def helper(time, i):
            if i == len(courses):
                return 0
            maxTaken = helper(time, i + 1) # not take current course
            if time + courses[i][0] <= courses[i][1]:
                maxTaken = max(maxTaken, 1 + helper(time + courses[i][0], i + 1)) # take current course
            return maxTaken
        
        return helper(0, 0)

"""
- greedy (*2) with priority queue 
- O(nlogn), O(n)
"""
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        pq = []
        start = 0
        for t, end in sorted(courses, key = lambda x: x[1]): # greedily take courses that ends earlier
            start += t
            heapq.heappush(pq, -t)
            while start > end: # when don't have enough time to take current course, greedily "unlearn" previously taken course with largest duration
                start += heapq.heappop(pq)
        return len(pq)

s = Solution()
s.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])