"""
- hashmap
- O(nlogn + comb(n/u)), O(n)
"""
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        info = sorted(zip(timestamp, username, website), key= lambda x: x[0])
        user_websites = defaultdict(list)
        for t, u, w in info:
            user_websites[u].append(w)
        score = 0
        best_pattern = []
        
        pattern_count = Counter()
        for websites in user_websites.values():
            patterns = set(itertools.combinations(websites, 3))
            for p in patterns:
                pattern_count[p] += 1
                if pattern_count[p] > score or (pattern_count[p] == score and p < best_pattern):
                    score = pattern_count[p]
                    best_pattern = p       
        return best_pattern