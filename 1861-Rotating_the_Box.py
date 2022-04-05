"""
- 2D Array
- O(mn), O(mn)
- can be optimized using two pointers (one for available slot, the other for stone)
"""
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        M, N = len(box), len(box[0])
        rotated_box = [["."] * M for _ in range(N)]
        
        
        for r in range(M):
            bottom_pos = c = N - 1 # bottom_pos: current bottom pos where the stone group will land on
            while c >= 0:
                stone_group_count = 0
                while c >= 0 and box[r][c] != "*":
                    if box[r][c] == "#":
                        stone_group_count += 1
                    c -= 1
                # mark obstacle
                if c >= 0: rotated_box[c][M-1-r] = "*"
                # move stones to current bottom
                for k in range(bottom_pos, bottom_pos - stone_group_count, -1): 
                    rotated_box[k][M-1-r] = "#"
                bottom_pos = c - 1
                c -= 1
        return rotated_box