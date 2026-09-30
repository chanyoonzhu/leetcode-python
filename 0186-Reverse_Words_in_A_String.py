class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """  
        def reverseLeftToRight(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1; r -= 1
        
        l, r = 0, len(str)-1
        reverseLeftToRight(str, l, r)
        l = r = 0
        while r < len(str):
            while r < len(str) and str[r] != " ": # df the first condition for the end of the list
                r += 1
            reverseLeftToRight(str, l, r-1)
            r += 1; l = r

sl = Solution()
print(sl.reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))