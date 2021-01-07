import heapq

class Solution(object):

    """
    - greedy with heap - failed: [[5,5],[4,6],[2,6]] output: 1 expected: 2
    """
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        pq = [(d, t) for t, d in courses]
        heapq.heapify(pq)
        total_duration, total_courses = 0, 0
        while pq:
            d, t = heapq.heappop(pq)
            if total_duration + t <= d:
                total_duration += t
                total_courses += 1
        return total_courses

    """
    - greedy with heap - correct answer
    - O(nlogn), O(n)
    - algorithm: greedy, picking courses taking less time over those taking longer time
    1. sort courses by close day
    2. iterate courses, in each iteration, check if taking the course violates "finish before close day" rule
    3. if rule is violated, remove the previously iterated course that needs the longest time (using a priority queue)
    """
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        pq = []
        start = 0
        for t, end in sorted(courses, key = lambda x: x[1]):
            start += t
            heapq.heappush(pq, -t)
            while start > end:
                start += heapq.heappop(pq)
        return len(pq)

s = Solution()
s.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])