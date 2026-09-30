class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        """
        - Caveat: 
        - can have leading 0s
        - 1.0 1 should be 0
        """

        version1Arr = version1.split('.')
        version2Arr = version2.split('.')
        diff = len(version1Arr) - len(version2Arr)
        if diff > 0:
            version2Arr += ['0'] * diff
        else:
            version1Arr += ['0'] * (-diff)
        
        def helper(arr1, arr2):
            if not arr1 and not arr2:
                return 0
            if int(arr1[0]) > int(arr2[0]):
                return 1
            elif int(arr1[0]) < int(arr2[0]):
                return -1
            else:
                return helper(arr1[1:], arr2[1:])
        
        return helper(version1Arr, version2Arr)