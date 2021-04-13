class RandomizedCollection(object):

    """
    - array + hashmap + hashset
    - similar question: 380
    - caveat: since dups allowed, the dictionary value can't just be a list because item search is not O(1), has to use a hashset
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = collections.defaultdict(set)
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        doesContain = False
        if self.pos[val]:
            doesContain = True
        self.nums.append(val)
        self.pos[val].add(len(self.nums) - 1)
        return doesContain
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.pos[val]:
            return False
        index, last, last_index = self.pos[val].pop(), self.nums[-1], len(self.nums) - 1 # self.pos[val][-1] won't work on set, has to use self.pos[val].pop()
        self.nums[index] = last
        self.pos[last].add(index)
        self.pos[last].remove(last_index)
        self.nums.pop()
        return True
        
        
    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        index = random.randint(0, len(self.nums) - 1)
        return self.nums[index]
        


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

