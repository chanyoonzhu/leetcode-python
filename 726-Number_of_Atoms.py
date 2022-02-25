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
                        
                