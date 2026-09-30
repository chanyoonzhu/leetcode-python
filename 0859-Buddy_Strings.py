"""
- String
- O(n), O(1)
"""
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        N = len(s)
        if N != len(goal):
            return False
        
        diff_s = list()
        diff_goal = list()
        
        for i in range(N):
            if s[i] != goal[i]:
                if len(diff_s) > 2: return False
                diff_s.append(s[i])
                diff_goal.append(goal[i])
        
        if len(diff_s) == len(diff_goal) == 2 and diff_s == diff_goal[::-1]:
            return True
        
        if len(diff_s) == len(diff_goal) == 0 and len(set(list(s))) < N: # easy to miss: repetitive letters in s
            return True
        
        return False
        