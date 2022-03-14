"""
- walking backwards
- O(max(tx, ty)), O(1)
"""
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx <= tx and sy <= ty:
            if sx == tx and sy == ty:
                return True
            if tx > ty:
                tx -= ty
            else:
                ty -= tx
        return False

"""
- modulo: todo
"""
        