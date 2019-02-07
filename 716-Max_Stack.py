import heapq

class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = [] # normal stack
        self.s2 = [] # max element at each s1 push
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.s1.append(x)
        if self.s2:
            self.s2.append(max(x, self.s2[-1]))
        else:
            self.s2.append(x)

        
    def pop(self):
        """
        :rtype: int
        """
        self.s2.pop()
        return self.s1.pop()
   

    def top(self):
        """
        :rtype: int
        """
        return self.s1[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.s2[-1]

    def popMax(self):
        """
        :rtype: int
        """
        max_ = self.s2.pop()
        temp = [] # items coming after max in s1
        while self.s1[-1] != max_:
            temp.append(self.pop()) # pop until find max in s1
        
        self.s1.pop() # pop max
        
        while temp:
            self.push(temp.pop()) 
        
        return max_

# Your MaxStack object will be instantiated and called as such:
obj = MaxStack()
obj.push(2)
obj.push(1)
obj.push(5)
obj.push(3)
obj.push(9)

param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.peekMax()
param_5 = obj.popMax()