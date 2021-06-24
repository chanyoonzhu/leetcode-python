"""
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.


Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []
 
Constraints:

1 <= slots1.length, slots2.length <= 10^4
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 10^9
1 <= duration <= 10^6 
"""

"""
Clarification questions:
Q: Are the time slots sorted for each person
A: Order is not guaranteed
Q: In each available time, can the end time be smaller than start time?
A: No, you can assume end time is always larger than start time
Q: Between two available times for a single person, could there be an overlap? For example, [[10,20],[15,30]]
A: You can assume this will not happen
"""

"""
- two pointers, sweep lines
- time: O(max(mlog(m), nlog(n))) sorting:O(max(mlog(m), nlog(n))) and iteration O(max(m, n))
- space: O(n) for sorting
"""
class Solution(object):
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if end - start >= duration:
                return [start, start + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        
        return []

"""
- heap: push all available time tuples from both slots into one priority queue
- O(max(mlog(m), nlog(n))), log(m) for each pop, pop m times in worst scenario
- algorithm:
1. remove available time tuples from slots list if available time is smaller than duration
2. put all available time tuples from both slots into a priority queue (min heap)
3. pop from heap and see if available time tuple popped has an interval with top of heap (next available time tuple) larger than duration, if yes, return interval
4. heap pops until empty and returns []

"""
class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        heap = [[start, end] for start, end in slots1 + slots2 if end - start >= duration] # not just for performance, remove this also ruins the logic
        # or: list(filter(lambda slot: slot[1] - slot[0] >= duration, slots1 + slots2))
        heapq.heapify(heap)
        
        while len(heap) > 1: # need at least 1 to peek
            if heapq.heappop(heap)[1] - heap[0][0] >= duration:
                return [heap[0][0], heap[0][0] + duration]
        return []