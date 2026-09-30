"""
- hashmap
- add: O(1), O(n), find: O(n), O(1)
- trade-off: other solution is to add all possible sums to a set as we add, that would reverse the time complexity of add and find
"""
class TwoSum:

    def __init__(self):
        self.num_counts = Counter() # needs count because edge case: num * 2 = target
        

    def add(self, number: int) -> None:
        self.num_counts[number] += 1
        

    def find(self, value: int) -> bool:
        for num in self.num_counts.keys():
            other_num = value - num
            if other_num in self.num_counts:
                if num != other_num or self.num_counts[other_num] > 1: # easy to miss: num == other_num
                    return True
        return False