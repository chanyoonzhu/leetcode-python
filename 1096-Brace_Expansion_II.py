"""
- recursion
- O(n), O(n)
"""
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def helper(expression):
            res = [[]] # each inner list holds expression groups delimited by ","
            cur = ""
            i = 0
            while i < len(expression):
                c = expression[i]
                if c.isalpha():
                    cur += c
                else:
                    if cur: 
                        if not res[-1]:
                            res[-1].append(cur)
                        else:
                            for k in range(len(res[-1])):
                                res[-1][k] = res[-1][k] + cur
                    if c == ",":
                        res.append([])
                    elif c == "{":
                        inner_res, consumed = helper(expression[i+1:])
                        i += consumed
                        if not res[-1]:
                            res[-1].extend(inner_res)
                        else:
                            combined = []
                            for exp1 in res[-1]:
                                for exp2 in inner_res:
                                    combined.append(exp1 + exp2)
                            res[-1] = combined
                    elif c == "}":
                        combined_res = sorted(set([exp for group in res for exp in group])) # easy to miss: dedup and sort
                        return (combined_res, i + 1)
                    cur = ""
                i += 1
            combined_res = sorted(set([exp for group in res for exp in group]))
            return (combined_res, i)
        return helper(expression + ",")[0]
        