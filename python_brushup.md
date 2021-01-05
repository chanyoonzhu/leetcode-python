# Numbers
- define largest/smallest int: 
```
largest = float("inf") 
smallest = float("-inf")
```

# List
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
dict_s = Counter(s)
dict_s # {"A": 1, "B": 1, "C": 2, "D": 1}
```

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



