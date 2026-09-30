class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        cur_lower = lower
        for x in nums:
            if cur_lower > upper:
                break
            if x < cur_lower:
                continue
            if x > cur_lower:
                res.append(self.buildInterval(cur_lower, min(upper, x-1))) # easy to miss, min
            cur_lower = x + 1
        if cur_lower <= upper: # easy to miss: upper > nums[-1]
            res.append(self.buildInterval(cur_lower, upper))
        return res
    
    def buildInterval(self, low, high):
        if high == low:
            return str(low)
        else:
            return f"{low}->{high}"