"""
- topological sort
- O(V + E), O(V + E)
"""
class Solution:        
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        all_receipes = set(recipes)
        indegrees = defaultdict(int)
        graph = defaultdict(set)
        
        for recipe, items in zip(recipes, ingredients):
            indegrees[recipe] = len(items)
            for i in items:
                graph[i].add(recipe)
            
        res = []
        queue = deque(supplies)
        while queue: 
            item = queue.popleft()
            if item in all_receipes:
                res.append(item)
            for sub_item in graph[item]:
                indegrees[sub_item] -= 1
                if indegrees[sub_item] == 0: queue.append(sub_item)
        return res