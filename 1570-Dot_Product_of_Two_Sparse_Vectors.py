"""
- hashmap
- O(n), O(n)
"""
class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_to_value = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.index_to_value[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i in vec.index_to_value.keys():
            if i in self.index_to_value:
                result += vec.index_to_value[i] * self.index_to_value[i]
        return result