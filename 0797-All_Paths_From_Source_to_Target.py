"""
- dfs (DAG)
- O(n * 2^n), O(n * 2^n) - https://leetcode.com/problems/all-paths-from-source-to-target/solution/
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        return self.dfs(0, len(graph) - 1, graph, {})
           
    def dfs(self, start, target, graph, memo):
        if start == target:
            return [[target]]
        if (start, target) not in memo:
            paths = []
            for nei in graph[start]:
                for nei_path in self.dfs(nei, target, graph, memo):
                    paths.append([start] + nei_path)
            memo[(start, target)] = paths
        return memo[(start, target)]