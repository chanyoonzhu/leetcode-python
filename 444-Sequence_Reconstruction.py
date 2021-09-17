"""
- topological sort (with BFS)
"""
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        
        indexes = {n: i for i, n in enumerate(org)}
        in_degree = [-1] * len(org) # i: number - 1
        graph = collections.defaultdict(list)
        for seq in seqs:
            for i in range(len(seq)):
                if seq[i] not in indexes: return False # edge case: number in seq not in org
                if in_degree[seq[i] - 1] == -1: in_degree[seq[i] - 1] = 0 # edge case: a number in org doesn't show up in seq
                if i > 0: 
                    graph[seq[i - 1]].append(seq[i])
                    in_degree[seq[i] - 1] += 1
        
        queue = [i + 1 for i, c in enumerate(in_degree) if c == 0]
        idx = 0
        while queue:
            if len(queue) > 1: return False
            if idx != indexes[queue.pop(0)]: return False
            for n in graph[org[idx]]:
                in_degree[n - 1] -= 1
                if in_degree[n - 1] == 0: queue.append(n)
            idx += 1
        return idx == len(org)

"""
- Logic (with hashmaps)
- Must satisfy 2 conditions: 1. Every sequence in seqs should be a subsequence in org; 2.Every 2 consecutive elements in org should be consecutive elements in some sequence from seqs
"""
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        
        if not seqs: return False # edge case: seqs can be []
        
        indexes_org = {n: i for i, n in enumerate(org)}
        
        indexes_seq = collections.defaultdict(list)
        for i, seq in enumerate(seqs):
            for j in range(len(seq)):
                indexes_seq[seq[j]].append((i, j)) # prepares for condition 2
                if seq[j] not in indexes_org or j > 0 and indexes_org[seq[j]] <= indexes_org[seq[j - 1]]: # testing condition 1
                    return False
        
        # testing condition 2
        for i in range(1, len(org)):
            prev, cur, is_connected = org[i - 1], org[i], False
            for ii, jj in indexes_seq[prev]:
                if jj < len(seqs[ii]) - 1 and seqs[ii][jj + 1] == cur:
                    is_connected = True
            if not is_connected: return False
        return True

"""
- Logic (with hashmaps) - simplifies condition 2 testing
- Must satisfy 2 conditions: 1. Every sequence in seqs should be a subsequence in org; 2.Every 2 consecutive elements in org should be consecutive elements in some sequence from seqs
"""
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        
        if not seqs: return False
        
        indexes_org = {n: i for i, n in enumerate(org)}
        
        pairs = set()
        
        for i, seq in enumerate(seqs):
            for j in range(len(seq)):
                if j > 0: pairs.add((seq[j - 1], seq[j])) # prepares for condition 2
                if seq[j] not in indexes_org or j > 0 and indexes_org[seq[j]] <= indexes_org[seq[j - 1]]: # testing condition 1
                    return False
        
        # testing condition 2
        for i in range(1, len(org)):
            if (org[i - 1], org[i]) not in pairs: return False
        return True