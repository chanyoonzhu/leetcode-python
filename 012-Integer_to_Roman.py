class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        sym = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M'], ['M']]
        e, base = 3, 10
        res = ""
        while e >= 0:
            div, mod = divmod(num, base ** e)
            if div == 0:
                e -= 1
                continue
            else:
                if div < 4:
                    res += (sym[e][0] * div)
                elif div == 4:
                    res += (sym[e][0] + sym[e][1])
                elif div == 5:
                    res += sym[e][1]
                elif div < 9:
                    res += (sym[e][1] + sym[e][0] * (div - 5))
                elif div == 9:
                    res += (sym[e][0] + sym[e][2])
            num = mod
            e -= 1
        return res