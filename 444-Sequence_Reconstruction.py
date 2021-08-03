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