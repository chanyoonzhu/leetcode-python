class CustomStack:

    """
    - stack with array
    - push: O(1), O(1); pop: O(1), O(1); inc:O(k), O(1)
    """
    def __init__(self, maxSize: int):
        self.nums = []
        self.max = maxSize
        

    def push(self, x: int) -> None:
        if len(self.nums) < self.max:
            self.nums.append(x)
        

    def pop(self) -> int:
        if self.nums:
            return self.nums.pop()
        return -1
        

    def increment(self, k: int, val: int) -> None:
        n = len(self.nums)
        for i in range(min(k, n)):
            self.nums[i] += val

    """
    - stack with array - optimized with lazy load (log increment in array, only increment when pop), inc[k] means for all elements stack[0] ~ stack[i],
        we should plus inc[i] when popped from the stack.
    - push: O(1), O(1); pop: O(1), O(1); inc:O(1), O(n)
    """
    def __init__(self, maxSize: int):
        self.nums = []
        self.max = maxSize
        self.inc = []
        

    def push(self, x: int) -> None:
        if len(self.nums) < self.max:
            self.nums.append(x)
            self.inc.append(0)
        

    def pop(self) -> int:
        if self.nums:
            num = self.nums.pop() + self.inc[-1]
            if len(self.inc) > 1:
                self.inc[-2] += self.inc[-1]
            self.inc.pop()
            return num
        return -1
        

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val