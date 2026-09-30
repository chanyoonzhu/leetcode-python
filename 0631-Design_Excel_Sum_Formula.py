"""
- recursion
"""
class Excel:

    # O(mn)
    def __init__(self, height: int, width: str):
        self.sheet = [[0] * (self._getNumerical(width) + 1) for _ in range(height + 1)] # stores values
        self.formula = [[list() for _ in range(self._getNumerical(width) + 1)] for _ in range(height + 1)] # stores formula (as is)

    # O(1)
    def set(self, row: int, column: str, val: int) -> None:
        col = self._getNumerical(column)
        self.sheet[row][col] = val
        self.formula[row][col] = list() # easy to miss: clear formula
        

    # O((mn)^2)
    def get(self, row: int, column: str) -> int:
        col = self._getNumerical(column)
        if not self.formula[row][col]:
            return self.sheet[row][col]
        res = 0
        for f in self.formula[row][col]:
            f_elements = f.split(":")
            if len(f_elements) == 1: # a cell
                res += self.get(int(f_elements[0][1:]), f_elements[0][0]) # recursively get cell value
            else:  # a range
                start, end = f_elements
                for row in range(int(start[1:]), int(end[1:]) + 1): # eg: A1:B2  range(1, 3)
                    for col_ord in range(ord(start[0]), ord(end[0]) + 1): # eg: A1:B2  range(ord("A"), ord("B") + 1)
                        res += self.get(row, chr(col_ord)) # recursively get cell value
        return res
        
    # O((mn)^2)
    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        col = self._getNumerical(column)
        self.formula[row][col] = numbers
        return self.get(row, column)
        
    def _getNumerical(self, col: str):
        return ord(col) - ord("A")
    
        


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)