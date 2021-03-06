from collections import defaultdict

class Logger:

    """
    - hashmap
    - O(1), O(n)
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.message_to_time = dict()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.message_to_time or timestamp - self.message_to_time[message] >= 10:
            self.message_to_time[message] = timestamp # caveat: don't update timestamp if not printing this time
            return True
        return False

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)