"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

"""
- caveat: all subordinates, not just direct subordinates
- dfs
- O(n), O(n)
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapping = {}
        for emp in employees:
            mapping[emp.id] = (emp.importance, emp.subordinates)
        
        def dfs(id):
            imp = mapping[id][0]
            for s in mapping[id][1]:
                imp += dfs(s)
            return imp
    
        return dfs(id)