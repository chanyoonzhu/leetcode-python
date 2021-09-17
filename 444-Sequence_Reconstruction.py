"""
- topological sort (with BFS)
- many corner cases
"""
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        N = len(org)
        edges = collections.defaultdict(set)
        degrees = [0] * N
        indexes = {}
        vals = set()
        
        for i, n in enumerate(org):
            indexes[n] = i
            
        for seq in seqs:
            for i in range(len(seq)):
                cur = seq[i]
                vals.add(cur)
                if cur not in indexes: return False # caveat: may not exist in org
                if i < len(seq) - 1:
                    nxt = seq[i + 1]
                    if nxt not in edges[cur]: # caveat: can have seq duplicates, only add once
                        edges[cur].add(nxt)
                        if nxt in indexes: # caveat: may not exist in org
                            degrees[indexes[nxt]] += 1
        
        org_i = 0
        q = [i for i in range(N) if not degrees[i]]  
        while len(q) == 1:
            i = q.pop()
            if i != org_i: return False
            org_i += 1
            if org[i] not in vals: return False # may not exist in seqs
            for nei in edges[org[i]]:
                degrees[indexes[nei]] -= 1
                if not degrees[indexes[nei]]:
                    q.append(indexes[nei])
        return org_i == N

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