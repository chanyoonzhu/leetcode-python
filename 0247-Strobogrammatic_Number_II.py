class Solution:

    """
    - resursion
    - O(n), O(n)
    """
    def findStrobogrammatic(self, n: int) -> List[str]:
        self.mapping = {"0": "0", "1": "1", "6":"9", "8":"8", "9":"6"}
        self.result = []
        self.i = 0
        
        def generate(n):
            if n == 0:
                return self.result
            if n == 1:
                k = len(self.result)
                if not k:
                    for c in ["0", "1", "8"]:
                        self.result.append(c)
                for _ in range(k):
                    curr = self.result.pop(0)
                    for c in ["0", "1", "8"]:
                        self.result.append(curr[:self.i] + c + curr[self.i:])
                return generate(n - 1)
            else:
                k = len(self.result)
                if not k:
                    for c1, c2 in self.mapping.items():
                        if c1 != "0":
                            self.result.append(c1 + c2)
                for _ in range(k):
                    curr = self.result.pop(0)
                    for c1, c2 in self.mapping.items():
                        self.result.append(curr[:self.i] + c1 + c2 + curr[self.i:])
                self.i += 1
                return generate(n - 2)
        
        return generate(n)

        """
        - better solution: # todo
        """
                
                
        