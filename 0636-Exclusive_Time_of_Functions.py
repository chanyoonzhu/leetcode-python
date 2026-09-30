"""
- clarification: function in lower stack cannot finish before function in a higher stack finishes
"""
"""
- stack
- O(n), O(n)
"""
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = [] # id, start_time
        result = [0] * n
        for log in logs:
            id_, type_, time = log.split(":")
            id_, time = int(id_), int(time)
            if type_ == "start":
                stack.append([id_, time]) 
            else:
                _, start_time = stack.pop()
                duration = time - start_time + 1
                result[id_] += duration
                if stack:
                    result[stack[-1][0]] -= duration # minus penalty
        return result