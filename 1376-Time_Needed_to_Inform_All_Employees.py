"""
- dfs
- O(V + E), O(V + E)
- key: can inform subordinates in parallel, time is the max among all subordinates, not the sum!
"""
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        org_struct = collections.defaultdict(list)
        for sub_id, manager_id in enumerate(manager):
            org_struct[manager_id].append(sub_id)
        return self.dfs(-1, org_struct, informTime)
        
    def dfs(self, id, org_struct, informTime):
        time = 0
        for sub_id in org_struct[id]:
            time = max(time, informTime[sub_id] + self.dfs(sub_id, org_struct, informTime))
        return time

"""
- bfs
- O(V + E), O(V + E)
"""
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        org_struct = collections.defaultdict(list)
        for sub_id, manager_id in enumerate(manager):
            org_struct[manager_id].append(sub_id)
        
        res = 0
        q = collections.deque([(-1, 0)])
        while q:
            manager_id, time = q.popleft()
            res = max(res, time)
            for sub_id in org_struct[manager_id]:
                q.append((sub_id, time + informTime[sub_id]))
        return res