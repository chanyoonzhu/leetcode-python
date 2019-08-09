class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        """
        from collections import defaultdict
        res = []
        dic = defaultdict(int)
        thresh = math.floor(len(nums) / 3)
        for num in nums:
            if dic[num] != -1:
                dic[num] += 1
                if dic[num] > thresh:
                    res.append(num)
                    dic[num] = -1
        return res
        """
        
        """
        - counter
        N = len(nums)
        count = collections.Counter(nums)
        res = []
        for n, t in count.items():
            if t > N / 3:
                res.append(n)
        return res
        """
        
        """
        - O(1) space
        - intuition: can be no more than 2 numbers that satisfies condition
        """
        res = []
        count1 = count2 = 0
        n1 = n2 = 0
        for n in nums:
            if n == n1:
                count1 += 1
            elif n == n2:
                count2 += 1
            elif count1 == 0:
                n1 = n
                count1 += 1
            elif count2 == 0:
                n2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -=1
            
        count1 = count2 = 0
        for n in nums:
            if n == n1:
                count1 += 1
            elif n == n2:
                count2 += 1
        
        if count1 > len(nums) / 3:
            res.append(n1)
        if count2 > len(nums) / 3:
            res.append(n2)
        
        return res

s = Solution()
s.majorityElement([2,2])