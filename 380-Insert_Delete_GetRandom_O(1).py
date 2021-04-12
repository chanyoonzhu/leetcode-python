class RandomizedSet(object):

    """
    - array and hashmap
    - intuition: set/hashmap can be used to create the insert/remove api pretty easily, but random needs random access so an array is needed
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = list()
        self.pos = dict()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos:
            return False
        self.nums.append(val)
        self.pos[val]= len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos:
            return False
        index = self.pos[val]
        last_val = self.nums[-1]
        self.nums[index] = last_val
        self.pos[last_val] = index # easy to forget
        self.nums.pop()
        del self.pos[val]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = random.randint(0, len(self.nums) - 1)
        return self.nums[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()