# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        """
        - O(nlog(n))
        - intuition: natural way of scheduling rooms
            * starting from earliest meetings
            * find the meeting that finish the earliest, if start time is smaller, create new room
              if start time is larger, update the finish of that room to this meeting's
            * use a heap to keep the room finish the earliest
            
        import heapq
        
        rooms = []
        for interval in sorted(intervals, key = lambda x: x.start): # have to start from earliest
            if not rooms:
                heapq.heappush(rooms, (interval.end, interval.start))
            else:
                end, start = rooms[0]
                if interval.start < end: # if start earlier than whoever ends the earlierest, assign new room
                    heapq.heappush(rooms, (interval.end, interval.start))
                else:
                    heapq.heappop(rooms)
                    heapq.heappush(rooms, (interval.end, interval.start))
        
        return len(rooms)
        """
        
    
        
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