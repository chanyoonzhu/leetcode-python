"""
- https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/solution/
- Similar: 380
- intuition: build upon 380, since dups allowed, the dictionary value can't just be a counter but instead a hashset (cannot be a list because O(n) for insertion deletion)
"""

"""
- array + hashmap + hashset
- all time O(1)
"""
class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.nums_to_indexes = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        is_present = val in self.nums_to_indexes
        self.nums_to_indexes[val].add(len(self.nums))
        self.nums.append(val)
        return not is_present
        

    def remove(self, val: int) -> bool:
        if val not in self.nums_to_indexes:
            return False
        remove_idx, last_idx = self.nums_to_indexes[val].pop(), len(self.nums) - 1
        last = self.nums[last_idx]
        self.nums[remove_idx] = last
        self.nums_to_indexes[last].add(remove_idx)
        self.nums_to_indexes[last].remove(last_idx)
        if len(self.nums_to_indexes[val]) == 0:
            del self.nums_to_indexes[val] # caveat: delete and pop at the end, since remove_idx can be the same as last idx
        self.nums.pop()
        return True
        

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
param_1 = obj.insert(1)
param_1 = obj.insert(1)
param_1 = obj.insert(2)
param_1 = obj.insert(1)
param_1 = obj.insert(2)
param_1 = obj.insert(2)
param_2 = obj.remove(1)
param_2 = obj.remove(2)
param_2 = obj.remove(2)
param_2 = obj.remove(2)
param_3 = obj.getRandom()

