class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        
        nums = set([c for c in time if c != ':'])
        
        h, m = time[:2], time[3:]
        curr = int(h) * 60 + int(m)
        
        for i in range(1, 60 * 24 + 1): # df: +1 for 00:00
            hnew, mnew = divmod(curr + i, 60)
            hnew = hnew % 24
            hc = str(hnew) if len(str(hnew)) == 2 else '0' + str(hnew)
            mc = str(mnew) if len(str(mnew)) == 2 else '0' + str(mnew)
            valid = True
            for c in hc:
                if c not in nums:
                    valid = False
            for c in mc:
                if c not in nums:
                    valid = False
            if valid:
                return hc + ':' + mc