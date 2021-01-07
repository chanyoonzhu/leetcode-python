# Numbers
- define largest/smallest int: 
```
largest = float("inf") 
smallest = float("-inf")
```

# List
- sort list
list.sort() # in-place
sorted(list) # returns a sorted list
- remove first element from list
    - modifies original list
        ```
        l = ['a', 'b', 'c', 'd']
        l.pop(0)
        ```
        ```
        l = ['a', 'b', 'c', 'd']
        del l[0]
        ```
    - returns new list without, original list not modified
        ```
        l = ['a', 'b', 'c', 'd']
        l_copy = l[1:]
        ```

# Dict
* defaultdict:
```
from collections import defaultdict
k_to_list = defaultdict(list)
k_to_list[k].append("value")

k_to_tuple = defaultdict(lambda: (0,0))
k_to_tuple[k] = (1,2)
```

* Counter
```
s = "ABCCD"
counter = Counter(s)
counter # {"A": 1, "B": 1, "C": 2, "D": 1}
counter.most_common(3) # [('C', 2), ('A', 1), ('B', 1)]
```

# heap

- max heap
```
heap = [4,3,5,7,1,2,6]
heapq.heapify([-v for v in heap]) # min-heap by default, in-place 
heap # [1,2,3,4,5,6,7]
```
```
nums = [4,3,5,7,1,2,6]
heapq.nlargest(4, nums) # returns [7,6,5,4]
```
- min heap
```
heap = [4,3,5,7,1,2,6]
heapq.heapify(heap) # in-place 
heap # [1,2,3,4,5,6,7]
```
```
nums = [4,3,5,7,1,2,6]
heapq.nsmallest(4, nums) # returns [1,2,3,4]
```
- heap peek
```
heap # [1, 3, 2, 7, 4, 5, 6]
heap[0] # 1
```
- heap push/pop
```
heap # [1, 3, 2, 7, 4, 5, 6]
heapq.heappop(heap) # 1
heap # [2, 3, 5, 7, 4, 6]
```
```
heap # [1, 3, 2, 7, 4, 5, 6]
heapq.heappush(heap, 8)
heap # [1, 3, 2, 7, 4, 5, 6, 8]
```
- tuples in heap (max-heap)
``` # get most frequent items
heap = [(-v, k) for k, v in count.items()]
heapq.heapify(heap)
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res
```

# stack
Python's built-in list type makes a decent stack data structure as it supports push and pop operations in amortized O(1) time. ... The list over-allocates its backing storage so that not every push or pop requires resizing and you get an amortized O(1) time complexity for these operations.
`
list.append() # add to top of stack
list.pop() # remove from top of stack
`

# deque
double-ended queue
`
from collections import deque
deq.popleft() # in-memory
deq.pop() # in-memory
deq.append(val) 
deq.appendleft(val) 
deq.reverse()
`

# Tips:
quick global variable - eg: 230#L20


