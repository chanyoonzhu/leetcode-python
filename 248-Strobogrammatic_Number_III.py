"""
- recursive
"""
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        low, high = int(low), int(high)
        low_len, high_len = self.getLength(low), self.getLength(high)

        candidates_high_len, candidates_low_len = [], []

        for length in range(low_len, high_len + 1):
            valid_of_length = self.getValid(self.getStrobogrammaticOfLength(length))
            if length == low_len:
                candidates_low_len.extend(valid_of_length)
            candidates_high_len.extend(valid_of_length)

        return len([x for x in candidates_high_len if x <= high]) - len([x for x in candidates_low_len if x < low])
        
    
    def getLength(self, x):
        """
        - get length of number
        """
        length = 0
        if x == 0:
            return 1
        while x:
            length += 1
            x //= 10
        return length

    def getValid(self, candidates):
        """
        - filter valid number
        """
        return [int(x) for x in candidates if x == "0" or x and not x.startswith("0")] # easy to miss: x == "0" is valid
        
    
    def getStrobogrammaticOfLength(self, length) -> bool:
        """
        return Strobogrammatic of given length (including leading "0", can be used for recursive calls)
        """
        if length == 0:
            return [""]
        if length == 1:
            return ["0", "1", "8"]
        pool = self.getStrobogrammaticOfLength(length - 2)
        res = []
        for x in pool:
            res.extend([
                "0" + x + "0",
                "1" + x + "1",
                "8" + x + "8",
                "6" + x + "9",
                "9" + x + "6"
            ])
        return res
     
        
s = Solution()
# print(s.strobogrammaticInRange("50", "1000")) 

print(s.strobogrammaticInRange("0", "0"))
        
        
        