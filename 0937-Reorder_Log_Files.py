class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        def f(log):
            id_, rest = log.split(' ', 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)
        
        return sorted(logs, key=f) # order according to function return value