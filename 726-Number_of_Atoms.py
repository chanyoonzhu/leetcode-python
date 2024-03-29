"""
- stack
- O(n^2) - need multiplication of prev chars, O(n)
"""
from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        stack = [] 
        # string for each parenthesis # counter element -> count
        # as soon as open p, append new item to stack until 
        # 1. (, repeat previous step recursively
        # 2. ), get multiplier, pop last item from stack, calc with multiplier, merge to the last counter in the stack
                
        def printFromCounts(counter):
            return ''.join([f"{key}{(counter[key] if counter[key] > 1 else '')}" for key in sorted(counter.keys())])
        
        i = 0
        cur_element = ""
        cur_multi = 0
        stack = []
        while i < len(formula):
            c = formula[i]
            if ord(c) in range(ord('A'), ord('Z') + 1): # element
                # parsing element and its count
                cur_element += c
                i += 1
                if i < len(formula) and ord(formula[i]) in range(ord('a'), ord('z') + 1):
                    cur_element += formula[i]
                    i += 1
                while i < len(formula) and formula[i].isdigit():
                    cur_multi = cur_multi * 10 + ord(formula[i]) - ord("0")
                    i += 1
                # adding element to stack
                if not stack:
                    stack.append(Counter({cur_element: (cur_multi if cur_multi else 1)})) # easy to miss: cur_multi needs to be set to 1 if is 0
                else:
                    stack[-1][cur_element] += (cur_multi if cur_multi else 1)
            else:
                if c == "(":
                    stack.append(Counter())
                    i += 1
                elif c == ")": # parsing multiplier, pop prev group, multiply and merge with previous element
                    i += 1
                    # get multiplier
                    while i < len(formula) and formula[i].isdigit():
                        cur_multi = cur_multi * 10 + ord(formula[i]) - ord("0")
                        i += 1
                    prev_counts = stack.pop()
                    if cur_multi:
                        for ele in prev_counts:
                            prev_counts[ele] = prev_counts[ele] * cur_multi
                    if not stack:
                        stack.append(prev_counts)
                    else:
                        stack[-1] += prev_counts
            cur_element = "" # easy to miss: reset
            cur_multi = 0
        return printFromCounts(stack[0])

    
"""
- recursion
- O(n), O(n)
"""
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        def helper(formula):
            counts = Counter()
            i = 0
            cur = ""
            count = 0
            while i < len(formula):
                c = formula[i]
                if c.isdigit():
                    count = count * 10 + ord(c) - ord("0")
                elif c.isalpha():
                    if ord(c) in range(ord('A'), ord('Z') + 1):
                        if cur: counts[cur] += (count if count else 1) # easy to miss: else 1
                        cur = c
                    elif ord(c) in range(ord('a'), ord('z') + 1):
                        cur += c
                    count = 0
                elif c == "(":
                    if cur: counts[cur] += (count if count else 1)
                    cur, count = "", 0
                    inner_counts, consumed = helper(formula[i+1:])
                    counts += inner_counts
                    i += consumed
                elif c == ")":
                    if cur: counts[cur] += (count if count else 1)
                    cur, count = "", 0
                    while i + 1 < len(formula) and formula[i+1].isdigit():
                        count = count * 10 + ord(formula[i+1]) - ord("0")
                        i += 1
                    for ele in counts:
                        counts[ele] *= (count if count else 1)
                    return (counts, i + 1)  
                i += 1
            return (counts, i)
             
        counts = helper(formula + "Y")[0]
        return ''.join([f"{ele}{counts[ele] if counts[ele] > 1 else ''}" for ele in sorted(counts)])
        
                        
                