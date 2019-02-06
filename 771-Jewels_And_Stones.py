class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        total = 0
        cnt = collections.Counter(list(S))
        for l in J:
            if l in cnt:
                total += cnt[l]
        return total