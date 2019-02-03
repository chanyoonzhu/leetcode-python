class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        else:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        
        # tricky: direct remove is O(n) due to index shifting. Has to swap with last item to achieve O(1) deletion
        if val in self.pos:  
            pos = self.pos[val]
            endVal = self.nums[-1]
            self.nums[pos] = endVal
            self.pos[endVal] = pos
            del self.pos[val]
            self.nums.pop()
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        
        import random
        return self.nums[random.randint(0, len(self.nums)-1)]
    
    def swap(self, i, j):
        self.pos[self.nums[i]] = j
        self.pos[self.nums[j]] = i
        temp = self.nums[i]
        self.nums[i] = self.nums[j]
        self.nums[j] = temp
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()