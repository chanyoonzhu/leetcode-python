"""
- set
- O(n*n*m), O(n*m)
"""
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favorites = [set(companies) for companies in favoriteCompanies]
        result = []
        for i in range(len(favorites)):
            is_subset = False
            for j in range(len(favorites)):
                if i != j and not (favorites[i] - favorites[j]): # set diff, or favorites[i].issubset(favorites[j])
                    is_subset = True
                    break
            if not is_subset: result.append(i)
        
        return result