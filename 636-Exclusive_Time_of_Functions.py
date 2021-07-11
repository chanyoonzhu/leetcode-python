"""
- stack with line sweep
- O(n), O(n)
"""
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n
        prev_time = 0
        for log in logs:
            id_, type_, time = log.split(":")
            id_, time = int(id_), int(time)
            if type_ == "start":
                if stack:
                    result[stack[-1]] += time - prev_time 
                stack.append(id_)
                prev_time = time
            else:
                result[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return result

"""
- stack
- O(n), O(n)
"""
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n
        prev_time = 0
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