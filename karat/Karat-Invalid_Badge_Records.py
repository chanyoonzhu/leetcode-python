"""
 badge_records = [
   ["Martha",   "exit"],
   ["Paul",     "enter"],
   ["Martha",   "enter"],
   ["Martha",   "exit"],
   ["Jennifer", "enter"],
   ["Paul",     "enter"],
   ["Curtis",   "enter"],
   ["Paul",     "exit"],
   ["Martha",   "enter"],
   ["Martha",   "exit"],
   ["Jennifer", "exit"],
 ]

 Expected output: ["Paul", "Curtis"], ["Martha"]
"""
from collections import defaultdict
class Solution:
    def invalidBadgeRecords(self, badge_records: list) -> list[list]:
        invalid_enter = set()
        invalid_exit = set()
        records = dict()
        for name, type in badge_records:
            if name not in records:
                records[name] = False # outside, true inside
            if type == "exit":
                if not records[name]:
                    invalid_enter.add(name)
                records[name] = False
            else:
                if records[name]:
                    invalid_exit.add(name)
                records[name] = True
        invalid_exit |= set(name for name, is_in in records.items() if is_in) # easy to miss: check who's still in
        return [list(invalid_exit), list(invalid_enter)]

s = Solution()
print(s.invalidBadgeRecords(
    [
   ["Martha",   "exit"],
   ["Paul",     "enter"],
   ["Martha",   "enter"],
   ["Martha",   "exit"],
   ["Jennifer", "enter"],
   ["Paul",     "enter"],
   ["Curtis",   "enter"],
   ["Paul",     "exit"],
   ["Martha",   "enter"],
   ["Martha",   "exit"],
   ["Jennifer", "exit"],
 ]
))