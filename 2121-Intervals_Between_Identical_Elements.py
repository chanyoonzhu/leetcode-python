"""
- array
- O(n), O(n)
"""
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        
        N = len(arr)
        res = [0] * N
        n_to_pos = collections.defaultdict(list)
        for i, x in enumerate(arr):
            n_to_pos[x].append(i)
        
        for x in n_to_pos:
            left_sum = right_sum = left_count = right_count = 0
            for i in range(1, len(n_to_pos[x])):
                right_sum += (n_to_pos[x][i] - n_to_pos[x][0])
                right_count += 1
            res[n_to_pos[x][0]] = right_sum
            for i in range(1, len(n_to_pos[x])):
                diff = n_to_pos[x][i] - n_to_pos[x][i-1]
                right_sum = right_sum - diff * right_count
                right_count -= 1
                left_count += 1
                left_sum = left_sum + diff * left_count
                res[n_to_pos[x][i]] = left_sum + right_sum
        return res