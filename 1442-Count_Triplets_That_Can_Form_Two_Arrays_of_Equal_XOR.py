"""
- two pointer
- O(n^2), O(1)
- intuition: a = b, then a ^ b = 0;  If a subarray XOR is zero, then any splitting point in this subarray will result in 2 subarrays with same XOR value.
    a ^ b ^ c == a ^ (b ^ c)
"""
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count, n = 0, len(arr)
        for i in range(n - 1):
            accu = arr[i]
            for k in range(i + 1, n):
                accu ^= arr[k]
                if accu == 0: count += k - i # the position of j doesn't matter as long as arr[i] ^ arr[i + 1] ... ^ arr[k] = 0
        return count

"""
- prefix sum
- O(n), O(n)
- intuition: https://tinyurl.com/yy79n8pp
"""
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix={0:[-1, 1]}
        res, _sum = 0, 0
        for i, n in enumerate(arr):
            _sum ^= n
            idxSum, idxCnt = prefix.get(_sum, [0, 0])
            res += (i - 1) * idxCnt - idxSum
            prefix[_sum]= [idxSum + i,idxCnt + 1]
        return res