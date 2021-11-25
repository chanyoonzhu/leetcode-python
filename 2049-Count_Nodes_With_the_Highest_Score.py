"""
- tree (dfs)
- O(n), O(n)
"""
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # can have at most three parts: left subtree, right subtree, others
        
        N = len(parents)
        score_counts = defaultdict(int)
        
        children_map = defaultdict(list)
        for i, parent in enumerate(parents):
            children_map[parent].append(i)
            
        self.find_tree_size(N, children_map, score_counts, 0)
        return score_counts[max(score_counts.keys())]
            
           
    def find_tree_size(self, full_size, children_map, score_counts, node) -> int:
        score, children_count = 1, 0
        for child in children_map[node]:
            child_count = self.find_tree_size(full_size, children_map, score_counts, child)
            score *= (child_count if child_count else 1)
            children_count += child_count
        up_count = full_size - 1 - children_count # number of other nodes
        score *= (up_count if up_count else 1)
        score_counts[score] += 1
        return children_count + 1