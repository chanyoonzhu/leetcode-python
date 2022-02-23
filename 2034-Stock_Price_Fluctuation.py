from sortedcontainers import SortedDict

"""
- treemap (sorted list) + hashmap
"""
class StockPrice:

    def __init__(self):
        self._price_to_count = SortedDict() # price to count
        self._time_to_price = {}
        self._latest_time = float('-inf')
        

    # log(n)
    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self._time_to_price:
            old_price = self._time_to_price[timestamp]
            self._price_to_count[old_price] -= 1
            if self._price_to_count[old_price] == 0:
                del self._price_to_count[old_price]
                
        if price in self._price_to_count:
            self._price_to_count[price] += 1
        else:
            self._price_to_count[price] = 1
        
        self._time_to_price[timestamp] = price
        self._latest_time = max(timestamp, self._latest_time)

    # log(1)
    def current(self) -> int:
        return self._time_to_price[self._latest_time]

    # log(n)
    def maximum(self) -> int:
        return self._price_to_count.peekitem(-1)[0]

    # log(n)
    def minimum(self) -> int:
        return self._price_to_count.peekitem(0)[0]

"""
- follow up: add drop
"""
from sortedcontainers import SortedDict

class StockPrice:

    def __init__(self):
        self.sorted_price_to_count = SortedDict()
        self.timestamp_to_price = dict()
        self.latest_timestamp = 0
        

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.latest_timestamp:
            self.latest_timestamp = timestamp
        if timestamp in self.timestamp_to_price:
            prev_price = self.timestamp_to_price[timestamp]
            self.sorted_price_to_count[prev_price] -= 1
            if self.sorted_price_to_count[prev_price] == 0:
                del self.sorted_price_to_count[prev_price]
        self.timestamp_to_price[timestamp] = price
        self.sorted_price_to_count.setdefault(price, 0)
        self.sorted_price_to_count[price] += 1 
        
    def drop(self, timestamp: int) -> None:
        if timestamp in self.timestamp_to_price:
            price = self.timestamp_to_price[timestamp]
            del self.timestamp_to_price[timestamp]
            self.sorted_price_to_count[price] -= 1
            if self.sorted_price_to_count[price] == 0:
                del self.sorted_price_to_count[price]
            if timestamp == self.latest_timestamp:
                self.latest_timestamp = max(self.timestamp_to_price.keys())
                

    def current(self) -> int:
        return self.timestamp_to_price[self.latest_timestamp]
        

    def maximum(self) -> int:
        return self.sorted_price_to_count.peekitem(-1)[0]
        

    def minimum(self) -> int:
        return self.sorted_price_to_count.peekitem(0)[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()