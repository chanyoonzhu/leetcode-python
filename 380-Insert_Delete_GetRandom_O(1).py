"""
- array and hashmap
- time complexity for all APIs: O(1)
- intuition: set/hashmap can be used to create the insert/remove api pretty easily, but random needs random access so an array is needed
- array removal at index i is O(n), can be optimized to O(1) if we remove the last element and switch the last element with the element at index i
"""
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.num_to_idx = {}
        
    def insert(self, val: int) -> bool:
        if val in self.num_to_idx:
            return False
        self.num_to_idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_idx:
            return False
        last_val = self.nums[-1]
        remove_idx = self.num_to_idx[val]
        self.nums[remove_idx] = last_val
        self.num_to_idx[last_val] = remove_idx
        self.nums.pop()
        del self.num_to_idx[val]
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()