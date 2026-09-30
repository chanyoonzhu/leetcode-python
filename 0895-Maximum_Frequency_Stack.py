"""
- hashmap + counter
"""
class FreqStack:

    def __init__(self):
        self.counts = Counter()
        self.freq_to_vals = defaultdict(list)
        self.max_freq = 0

    # O(1)
    def push(self, val: int) -> None:
        self.counts[val] += 1
        self.freq_to_vals[self.counts[val]].append(val)
        self.max_freq = max(self.max_freq, self.counts[val])
        
    # O(1)
    def pop(self) -> int:
        maxi = self.freq_to_vals[self.max_freq].pop()
        if len(self.freq_to_vals[self.max_freq]) == 0:
            self.max_freq -= 1
        self.counts[maxi] -= 1
        return maxi
        


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