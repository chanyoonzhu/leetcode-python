class Solution(object):
    """ 
    - Greedy: assign the cookie with smallest satisfaction to the child that needs smallest cookie
    - O(max(nlogn, mlogm)): sort-max(nlogn, mlogm) and iterate once-max(n, m)
    - O(max(n, m))
    """
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        
        i, satisfied = 0, 0
        for cookie in s:
            if i < len(g) and cookie >= g[i]:
                satisfied += 1
                i += 1
        return satisfied

    """ 
    - same solution with sort(): in-place list mutation, faster (no copy). While sorted() create a new iterable instead
    - Greedy: assign the cookie with smallest satisfaction to the child that needs smallest cookie
    - O(max(nlogn, mlogm)): sort-max(nlogn, mlogm) and iterate once-max(n, m)
    - O(max(n, m))
    """
    def findContentChildren(self, g, s):
        g.sort()    # 对需求因子进行排序，从小到大
        s.sort()    # 对糖果数组进行排序，从小到大
        satisfied  = 0  # 记录可以被满足孩子数
        cookie = 0  # 记录可以满足的糖果数
        while satisfied <len(g) and cookie < len(s):
            if g[satisfied] <= s[cookie]: 
                satisfied += 1
            cookie += 1
        return satisfied