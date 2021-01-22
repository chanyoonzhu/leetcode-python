from collections import defaultdict

"""
- Clarification questions:
Q: Do the timestamps keep increasing? A: Yes.
Q: Is it strict increasing? A: Yes
- Follow-up question:
Q: What if the timestamps is increasing but not strictly increasing?
"""
class TimeMap:

    """
    - binary search: and hashmap
    - set: O(1), O(n); get: (O(logn)), O(n) - space for the hashmap
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.k_to_v = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.k_to_v[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.k_to_v or self.k_to_v[key][0][0] > timestamp:
            return ""
        return self._binary_search(self.k_to_v[key], 0, len(self.k_to_v[key]) - 1, timestamp)
        
    def _binary_search(self, values, start, end, timestamp) -> str:
        if start == end:
            return values[start][1]
        mid = start + (end - start + 1) // 2
        if values[mid][0] > timestamp:
            end = mid - 1
        else:
            start = mid
        return self._binary_search(values, start, end, timestamp)
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)