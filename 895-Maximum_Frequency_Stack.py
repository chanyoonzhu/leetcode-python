class FreqStack(object):

    def __init__(self):
        self.stack = []
        self.cnt = collections.Counter()
        self.freq = collections.defaultdict(list)
        self.maxFreq = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.cnt[x] += 1
        self.freq[self.cnt[x]].append(x)
        self.maxFreq = max(self.maxFreq, self.cnt[x])
        

    def pop(self):
        """
        :rtype: int
        """
        res = self.freq[self.maxFreq].pop()
        if len(self.freq[self.maxFreq]) == 0:
            del self.freq[self.maxFreq]
            self.maxFreq -= 1
        self.cnt[res] -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())