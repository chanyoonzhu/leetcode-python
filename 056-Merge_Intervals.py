class Solution(object):
    """
    - sweep lines
    - O(nlog(n)), -O(n)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            if not result:
                result.append([start, end])
            else:
                if start > result[-1][1]:
                    result.append([start, end])
                else:
                    result[-1][1] = max(result[-1][1], end)
        return result