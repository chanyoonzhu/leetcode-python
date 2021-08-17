"""
- brute force
- O(nlogn), O(1)
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [i for i in range(n + 1)]
        for i in range(n + 1):
            ans[i] = sum(int(c) for c in str(bin(ans[i]))[2:])
        return ans

"""
- bitwise operation
- O(n), O(1)
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0]
        for i in range(1, n + 1):
            counter.append(counter[i >> 1] + i % 2) # if i is even, then same as half of the number, if i is odd, half of the number + 1
            # same as: counter.append(counter[i >> 1] + (x & 1))
        return counter