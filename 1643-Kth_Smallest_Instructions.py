"""
- math combinations
"""
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
                    
        r, c = destination
        
        res= []
        remain_down = r
        for remain_steps in range(r + c - 1, -1, -1):
            com = comb(remain_steps, remain_down) # if greedily choose 'H' at this step, how many ways to travel the rest
            if com >= k: # must choose 'H', since answer is in one of the "com"s
                res.append("H")
            else: # mush choose 'V', since answer is lexicographically larger than all in "'H' + com"s
                remain_down -= 1
                k -= com
                res.append("V")
                
        return ''.join(res)