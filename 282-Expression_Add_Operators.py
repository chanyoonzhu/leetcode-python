"""
- backtracking (dfs)
- O(3^N)?
- hard: multiplication takes precedence, so need to keep track of previsouly added/subtracted number to revert a step back when multiplication shows up
"""
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        N = len(num)
        res = []
    
        def dfs(left, prev_num, total, path):
            if left == N:
                if total == target:
                    res.append(path)
            else:
                cur_num = 0
                for i in range(left, N):
                    cur_num = (cur_num * 10) + ord(num[i]) - ord("0")
                    if left == 0:
                        dfs(i+1, cur_num, total + cur_num, path + str(cur_num))
                    else:
                        # add
                        dfs(i+1, cur_num, total + cur_num, path + "+" + str(cur_num))
                        # subtract
                        dfs(i+1, -cur_num, total - cur_num, path + "-" + str(cur_num))
                        # multiply - prev_num stores the previously added/subtracted num with sign
                        dfs(i+1, prev_num * cur_num, total - prev_num + prev_num * cur_num, path + "*" + str(cur_num))
                    if num[left] == "0":
                        break
                        
        dfs(0, 0, 0, "")
        return res