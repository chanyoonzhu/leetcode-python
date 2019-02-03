class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        """
        since dups allowed, the dictionary value can't just be a number, it has to be a collection of numbers
        (array, set, queue)
        - can't use array and queue because item search is not O(1)
        """
        self.pos = collections.defaultdict(set)
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        unseen = True
        if val in self.pos:
            unseen = False
        self.pos[val].add(len(self.nums))
        self.nums.append(val)
        return unseen
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """

        if val not in self.pos:
            return False
        pos, lastVal = self.pos[val].pop(), self.nums[-1]
        if len(self.nums) - 1 != pos:
            self.nums[pos] = lastVal
            self.pos[lastVal].remove(len(self.nums) - 1)
            self.pos[lastVal].add(pos)
        if len(self.pos[val]) == 0:
            del self.pos[val]
        self.nums.pop()
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        
        import random
        return self.nums[random.randint(0, len(self.nums)-1)]
        


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

