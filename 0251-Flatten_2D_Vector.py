"""
- with index pointers
- key: 1. row can have [] array, need to continuously go to next row to find next 2. next and hasNext can to be called independently, must find current valid in both methods
"""
class Vector2D:

    """
    - O(1)
    """
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.r = 0
        self.c = 0

    """
    - O(N/c) or O(1)
    """
    def next(self) -> int:
        self.find_cur_valid()
        cur = self.vec[self.r][self.c]
        self.c += 1
        return cur
        

    """
    - O(N/c) or O(1)
    """
    def hasNext(self) -> bool:
        self.find_cur_valid()
        return self.r < len(self.vec)
    
    def find_cur_valid(self):
        while self.r < len(self.vec) and self.c == len(self.vec[self.r]): # easy to miss: row can have [] array, need to continuously skip
            self.r += 1
            self.c = 0

"""
- convert to 1D (more space needed)
"""
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()