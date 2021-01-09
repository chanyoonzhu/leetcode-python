class Solution(object):
    """
    - priority queue
    - O(nlog(n)), O(n) - worst case one room per meeting
    - intuition: natural way of scheduling rooms
        * starting from earliest meetings
        * find the meeting that finish the earliest, if start time is smaller, create new room
            if start time is larger, update the finish of that room to this meeting's
        * use a heap to keep the room finish the earliest
    """
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        intervals = sorted(intervals, key = lambda x: x[0])
        pq = [] # stores the current end time of each meeting room
        for start, end in intervals:
            if not pq:
                heapq.heappush(pq, end)
            else:
                if pq[0] <= start:
                    heapq.heappop(pq)
                heapq.heappush(pq, end)
        return len(pq)

    
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
        # res - largest number of rooms used at the same time of all history
        # rooms - number of rooms used at the same time at the time being
        # dic - key: start or end time; value: start ++1/end --1/end and start 0
        """
        res = rooms = 0
        dic = collections.defaultdict(int)
        
        for interval in intervals:
            dic[interval.start] += 1
            dic[interval.end] -= 1
        
        for time in sorted(dic.items(), key=lambda x:x[0]):
            rooms += time[1]
            res = max(res, rooms)
        
        return res