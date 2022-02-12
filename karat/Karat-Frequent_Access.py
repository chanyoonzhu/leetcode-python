"""
list of [name, time], time is string format: '1300' -> 13:00PM
return: list of names and that has more than three badge swipes within one hour.
name1: time1, time2, time3...
name2: time1, time2, time3, time4, time5...
example:
input: [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']] 
output: {
'Martha': ['1600', '1620', '1530']
}
"""
from collections import defaultdict

class Solution:
    def frequentAccess(self, accesses: list[list]) -> list:
        name_to_times = defaultdict(list)
        for name, time_str in accesses:
            time = int(time_str)
            name_to_times[name].append(time)
        
        res = []
        for name in name_to_times.keys():
            times = sorted(name_to_times[name])
            r = 0
            for l in range(len(times)):
                while r < len(times) and times[r] - times[l] <= 60:
                    r += 1
                if r - l >= 2:
                    res.append(name)
                    break
        return res

s = Solution()
print(s.frequentAccess([['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']]))
        