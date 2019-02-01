"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        """
        - greedy
        """

        import heapq
        
        rooms = [] # a min heap logging the current end time for each room
        
        intervals = sorted(intervals, key=lambda x: x.start)
        for interval in intervals:
            if len(rooms) == 0:
                heapq.heappush(rooms, interval.end)
            else:
                earliest = heapq.heappop(rooms) # find room that has the earliest ending time, see if can put in the same room 
                if earliest <= interval.start:
                    heapq.heappush(rooms, interval.end)
                else: # create new room
                    heapq.heappush(rooms, earliest)
                    heapq.heappush(rooms, interval.end)
        return len(rooms)

        """
        # res - largest number of rooms used at the same time of all history
        # rooms - number of rooms used at the same time at the time being
        # dic - key: start or end time; value: start ++1/end --1/end and start 0
        
        res = rooms = 0
        dic = {}
        
        intervals = sorted(intervals, key=lambda x: x.start)
        
        for interval in intervals:
            if interval.start not in dic:
                dic[interval.start] = 1
            else:
                dic[interval.start] += 1
            if interval.end not in dic:
                dic[interval.end] = -1
            else:
                dic[interval.end] -= 1  
        
        sortedDic = sorted(dic.items(), key=lambda x:x[0])
        for item in sortedDic:
            rooms += item[1]
            res = max(res, rooms)
            
        return res
        """
        
        
        