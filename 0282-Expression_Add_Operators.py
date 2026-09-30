"""
- backtracking
- O(3^N)
- hard: multiplication takes precedence, so need to keep track of previsouly added/subtracted number to revert a step back when multiplication shows up
"""
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        res = []
        
        def backtrack(i, prev_num, path, total): # prev_num is for multiplication calculation
            if i == N:
                if total == target:
                    res.append(path)
            else:
                cur_num = 0     
                for j in range(i, N):
                    cur_num = cur_num * 10 + ord(num[j]) - ord("0")
                    if i == 0:
                        backtrack(j+1, cur_num, path + str(cur_num), total + cur_num)
                    else:
                        # add
                        backtrack(j+1, cur_num, path + "+" + str(cur_num), total + cur_num)
                        # subtract
                        backtrack(j+1, -cur_num, path + "-" + str(cur_num), total - cur_num)
                        # multiply
                        backtrack(j+1, prev_num * cur_num, path + "*" + str(cur_num), total - prev_num + prev_num * cur_num)
                    if num[i] == "0": # easy to miss: cur_name can only be 0 and break to avoid concatenating with other digits
                        break
        backtrack(0, 0, "", 0)
        return res