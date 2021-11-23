"""253-Meeting_Rooms_II
- priority queue - each element keeps the current end time of a room
- O(nlog(n)), O(n) - worst case one room per meeting
- intuition: natural way of scheduling rooms
    * starting from earliest meetings
    * find the meeting that finish the earliest, if start time is smaller, create new room
        if start time is larger, update the end time of that room to this meeting's end time
    * use a heap to keep the room finish the earliest
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, key=lambda x: x[0])
        heap = []
        
        for start, end in intervals:
            if heap and heap[0] <= start: # greedily check against the meeting that ends the earliest. If meeting ended, pop the room since it's now available
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        
        return len(heap)

    
"""
- two pointers: smart solution, not very intuitive
- Algorithm:
1. Separate out the start times and the end times in their separate arrays.
2. Sort the start times and the end times separately. Note that this will mess up the original correspondence of start times and end times. They will be treated individually now.
3. We consider two pointers: s_ptr and e_ptr which refer to start pointer and end pointer. The start pointer simply iterates over all the meetings and the end pointer helps us track if a meeting has ended and if we can reuse a room.
4. When considering a specific meeting pointed to by s_ptr, we check if this start timing is greater than the meeting pointed to by e_ptr. If this is the case then that would mean some meeting has ended by the time the meeting at s_ptr had to start. So we can reuse one of the rooms. Otherwise, we have to allocate a new room.
5. If a meeting has indeed ended i.e. if start[s_ptr] >= end[e_ptr], then we increment e_ptr.
6. Repeat this process until s_ptr processes all of the meetings.
"""
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])
        starts.sort()
        ends.sort()
        
        ptr1 = ptr2 = 0
        n = len(intervals)
        rooms = 0
        while ptr1 < n and ptr2 < n:
            start, end = starts[ptr1], ends[ptr2]
            if start < end:
                rooms += 1
                ptr1 += 1
            else:
                ptr1 += 1
                ptr2 += 1
    
"""
- two pointers: same as previous solution but more intuitive
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        starts, ends = [], []
        for start, end in intervals:
            starts.append(start)
            ends.append(end)
            
        starts.sort()
        ends.sort()
        
        i = 0
        curr_room = max_room = 0
        for end in ends: # for each current smallest end, find how many starts before it
            while i < len(intervals) and starts[i] < end:
                curr_room += 1
                i += 1
            max_room = max(max_room, curr_room)
            curr_room -= 1
            
        return max_room
        
"""
- Line Sweeping
- O(n), O(n)
"""
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        res = curr = 0
        times = []
        for start, end in intervals:
            times.append((start, 1))
            times.append((end, -1))
        times.sort()
        for time, _type in times:
            curr += _type
            res = max(curr, res)
        return res