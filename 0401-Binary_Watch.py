class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        """
        - Convert all combination of time to bits, not all bits combinations to time
        """
        res = []
        for h in range(12):
            for m in range(60):
                # or bin(h * 64 + m)
                if (bin(h) + bin(m)).count('1') == num:
                    res.append("%d:%02d" % (h, m))
        return res