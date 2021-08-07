two sum: 1, 167


all, any: 833
array: 54,56,73,151,157,186,238,268,349,350,380,381,849,1146,1371,1381,1567
backtracking: 17,46,47,78,90,301,491,698,996,1593,1239,1307,1681,1718,1723
bfs: 79,103,116,127,133,200,207,210,212,297,301,399,529,743,752,785,787,803,863,959,971,987,1236,1306,1345,1654,1778
binary search:33,57,222,240,259,275,295,374,410,774,875,911,1011,1055,1146,1231,1272,1283,1428,1482,1552,1608,1648,1723,1802,1870
bit manipulation: 268,473,491,698,1371,1442,1542,1593,1681
bst: 99,230,333,490,729
bucket:299
circular array: 213,1658
divide and conquer: 53,215,241,307,308,312,327,395,973,1000,1039,1547
dfs: 17,79,91,99,105,106,113,124,129,133,200,207,210,212,230,236,241,261,297,298,301,329,331,333,337,399,490,529,549,666,687,695,743,753,778,785,787,803,863,947,959,975,987,1028,1236,1306,1340,1569,1644,1676,1740,1766,1778
dynamic programming: 5,10,32,39,45,53,55,70,72,91,97,139,198,213,279,312,322,403,410,416,435,473,494,518,562,583,712,746,1000,1035,1039,1143,1155,1312,1314,1458,1547,1696
graph: 785,863
greedy: 45,53,55,135,410,435,455,621,630,678,774,785,875,1011,1231,1353,1383,1402,1428,1482,1520,1537,1552,1567,1648,1665,1718,1775,1802,1851,1870
hashmap: 1,15,76,106,138,146,149,159,169,229,299,327,336,340,359,380,381,392,398,403,432,437,496,560,666,895,930,974,1000,1055,1371,1442,1542,1577,1590,1644
hashset: 1,381,432
heap: 23,215,218,253,295,347,621,630,759,778,973,1229,1353,1383,1696,1834,1851
inorder: 99,105,230,333
linked list: 2,21,24,25,86,138,146,382,432,445,587,705,706,1650
map: 205
math:12,149,168,268,391,470,621,794,836,1041,1344,1569
merge sort: 315,1574
misc:169,229(moore voting)
preorder: 105,106,113,331,437,545,666,971,987,1028,1569
queue:232,239,1696
range sum: 307,308,327,1314,930,1442
recursive: 2,116,241,247,273,450
segment tree: 307,308,327,850
sliding window: 3,76,159,209,239,340,395,904,930,992,1004,1052,1234,1358,1423,1498,1537,1574,1577,1658,1696,1793
sort: 56,99,164,179,252,280,315,524,581,L391,1300,1608
stack: 20,32,84,155,227,232,331,402,456,496,503,581,636,678,739,856,901,907,946,962,975,1019,1028,1063,1124,1130,1249,1381,1541,1597,1673,1856
string: 151,157,165,722,833,929,1520
topological sort: 207,210,329,444
tree: 116,222,235,236,333,337,450,298,549,687,729,1644,1650,1676,1740
trie: 208,211,212,336
two pointers: 15,42,76,86,121,159,167,209,253,259,392,524,581,680,904,986,1055,1229,1537,1574,1577,1658,1775,1868
union find: 323,778,947
zip: 833


## backtracking 
    - eg: 17-Letter Combinations of a Phone Number; 78-Subsets(classic)|90-Subsets II|46-Permutations|47-Permutations II; 491-Increasing Subsequences; 996-Number of Squareful Arrays; 1239; 698-Partition to K Equal Sum Subsets; 1593-Split a String Into the Max Number of Unique Substrings; 1681-Minimum Incompatibility; 1307-Verbal Arithmetic Puzzle(hard); 1718-Construct the Lexicographically Largest Valid Sequence (with greedy); 1723. Find Minimum Time to Finish All Jobs(hard, with binary search)

## binary search
- Key words:
find, sorted
- Three templates
1. when loop ends, start + 1 = end
```
start, end = 0, len(n) - 1
while start + 1 < end: 
    mid = start + (end - start) // 2
    if nums[mid] < target:
        start = mid
    else:
        end = mid
```
2. When loop ends, start = end
```
start, end = 0, len(n)
while start < end: # when loop ends, start = end
    mid = start + (end - start) // 2
    if nums[mid] < target:
        start = mid + 1
    else:
        end = mid
```
3. when loop ends, start = end + 1
```
start, end = 0, len(n) - 1
while start <= end: 
    mid = start + (end - start) // 2
    if nums[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
```
- My template:
    - strictly increasing find last one smaller than or equal to target
    ```
    start, end = 0, len(n) - 1  # use start = -1 or end = len(n) if returning -1 or len(n) is possible
    def bs(nums, start, end, target):
        if start == end:
            return start
        mid = start + (end - start + 1) // 2 # because start = mid, has to + 1 to shift to end or will be endless loop
        if nums[mid] > target: # use >, >=, <, <= based on specific case
            end = mid - 1
        else:
            start = mid
        return bs(nums, start, end, target)
    ```
    - strictly increasing find first one larger than or equal to target
    ```
    start, end = 0, len(n) - 1
    def bs(nums, start, end, target):
        if start == end:
            return start
        mid = start + (end - start) // 2 # because end = mid, don't + 1 to shift to start or will be endless loop
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid
        return bs(nums, start, end, target)
    ```
- tips
    - prevents int overflow:

        use:
        ```
        mid = start + (end - start) // 2
        ```
        not:
        ```
        mid = (start + end) // 2
        ```
- Examples: 57,911,1146(bisect), 278,374(basic), 981(strictly increasing, find lower), 315
- classic problems:
    - binary search + greedy: get the possible range of answer, binary search between range and see if current number can satisfy condition using greedy algorithm
        - eg: 410|774; 778-Swim in Rising Water(graph)|875|1011|1231|1283|1300|1482|1552|1648|1802(complex)|1870;1723-Find Minimum Time to Finish All Jobs(hard, with backtracking)

## Bit manipulation
- XOR
    - definition - same: 0, different: 1
    - types:
        - Subarray containing chars with certain conditions
            - tips: memoize the state of all prefixes in a hashmap, compute state using XOR
            - eg: 1371(even/odd),1542
        - Pure XOR: 1442,

## Bit-masking
- problems:
    - enumeration (can be solved using backtracking):
        - eg: 90-Subsets II; 491-Increasing Subsequences; 698-Partition to K Equal Sum Subsets; 1593-Split a String Into the Max Number of Unique Substrings; 1681-Minimum Incompatibility

## BFS
- key word: shorted path (eg. 1345); 
- algorithm: 
    elements: queue, visited hashset; 
    steps: while q, if q popped is target, finish, if not, add popped item's neighbors to the q; optimization: visited can be eliminated if allowed to change memory (mark on original data)
- classic problems:
    - all shortest paths: 301
    - 1D (array): 1654-Minimum Jumps to Reach Home 
    - String: 752-Open the Lock
    - Dijkstra's Algorithm: 743-Network Delay Time, 787-Cheapest Flights Within K Stops

## Divide and Conquer
- problems:
    - find subarrays with conditions:
        - eg: 53-Maximum Subarray

## Data Structure Implementation 
- summary: implement a data structure with required APIs and targeted complexity
- problems: 
    - hashset/hashmap implementation:
        - modulo with linkedlist/bst
        - eg: 705-Design HashSet, 706-Design HashMap
    - hashmap / doubly linked list: 146,380,381,432,460,1146,1381
    - stack: 
        155-Min Stack
    - heap: 295
    - Fenwick tree / segment tree: 307,308,327
- tips:
    use hashmap to achieve O(1) retrieval of a key
    use hashmap and doubly linked list to achieve retrieving min/max in O(1) eg:(LRU/LFU)146,432,460
    use Fenwick tree or Segment tree to solve range sum/max/min problem

## DFS - don't forget to reset visited back when all the branched dfs does not succeed.
- recursive (in-order)
```
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        print(node.val)
        dfs(node.right)
```
- iterative (in-order)
```
    stack = []
    while stack or node:
        if node:
            stack.append(node.left)
            node = node.left
        else:
            node = stack.pop()
            print(node.val)
            node = node.right
```
or 
```
    stack = []
    while stack or node:
        while node:
            stack.append(node.left)
            node = node.left
        node = stack.pop()
        print(node.val)
        node = node.right
```
- Inorder Morris*: O(n), O(1); eg.99
```
    node = root        
    while node:
        if node.left:
            temp = node.left
            while temp.right and temp.right != node:
                temp = temp.right
            if not temp.right: # when looking for prev, attach temp.right to node
                temp.right, node = node, node.left
                continue
            # when traversal, detach temp.right from node
            temp.right = None
        print(node.val)
        node = node.right

```
- Complexity: 
    - Time: O(n) - one visit each node
    - Space: O(n) - n stacks for skewed tree
- example: 230, 337; 778-Swim in Rising Water

## 2D DFS/BFS
- problems:
    - map hidden graph
        - eg: 1778-Shortest Path in a Hidden Grid; 1810-Minimum Path Cost in a Hidden Grid
    - find contiguous "islands"
        - eg: 959-Regions Cut By Slashes (need pixelating); 803-Bricks Falling When Hit (hard)
    - operation chaining:
        - eg: 399-Evaluate Division
    - other: 1766-Tree of Coprimes (hard)

## Dynamic programming -
backtracking with memoization; steps: build dp memory, define what dp[i] represents, find update function(s)
space can be optimized to O(1) if only need to track constant time of variables for each update
- Top down (depth-first-search): recursion using memoization
- Bottom up: loop using memoization (calculate those won't change first, eg.1143, 1340) - look at the transformation formula from the top-down solution to figure out what needs to be calculated first in the loop. Can use the subproblem size as the outer loop if dp(i, j) need dp(i + 1, j - 1) (eg.312，1312)
- types:
    - knapsack: 
        - 0/1 knapsack: 1049
        - tip: dp[_sum][i]
        - eg: 416, 494, 1049, 630-Course Schedule III
    - length in matrix: 562
    - reachable problem: 45,55
    - divide and conquer: 241
        - calculation among adjacent items: 312, 1039, 1547, 1000(hard)
            - tip: when bottom-up, use subproblem size as the outer loop
    - string subsequence with min/max cost: 97,516,583,1035,1092,1143,1458
        - edit-distance: 72,583,712,1312
    - number of ways to combine: knapsack?
        - eg: 1155-Number of Dice Rolls With Target Sum
    - subarray max/min:
        - eg: 53-Maximum Subarray

## Graph
- Complexity
    - time: O(N + E) N - number of nodes; E: number of edges
    - space: O(N)
- Algorithms: DFS and BFS
- Problems:
    - eg: 785-Is Graph Bipartite?
    - minimum cost path: Dijkstra Algorithm
        - eg: 743-Network Delay Time, 787-Cheapest Flights Within K Stops

## Greedy -
- instinct: 
Pick the locally optimal move at each step, and that will lead to the globally optimal solution.
Iterate over the array and update at each step the standard set for such problems: 1.current element 2.current local maximum sum (at this given point) 3.global maximum sum seen so far.
    - eg: 1402,1520,1665
- variations:
    - greedy with sort: 1775-Equal Sum Arrays With Minimum Number of Operations; 1537-Get the Maximum Score

## Heap - 
heapify time complexity: O(n), heap push/pop time complexity: O(logn)
- eg:
    - median: 295

## LinkedList
- tips:
    use dummy node to avoid checking edgecases 146
- problems:
    - find out the size of a circular linkedlist or the middle of the linkedlist
        - algorithm: fast and slow pointers
        - eg: 143-Reorder List
    - reverse a linkedlist:
        - eg: 143-Reorder List; 25-Reverse Nodes in k-Group

## Fenwick Tree (or binary index tree):
- used to solve numerous RANGE QUERY problems like finding minimum, maximum, sum, greatest common divisor, least common denominator in array in logarithmic time.
- eg: 307,308(2D),327(prefix-sum)
- can also use "Segment tree" to solve with more space

## Math
- permutation and combination
    - formula: P(n, r) = n! / (n - r)!   C(n, r) = n! / (r! * (n - r)!)
    - eg. 1569
- Gauss sum:
    - n + (n + 1) + ... + (n + k) = (n + n + k) * (k + 1) // 2
    - eg. 1648, 1802
- Sampling:
    - reservoir sampling: sampling in large/dynamic-size arrays with O(1) space
        - eg: 382-Linked List Random Node; 398-Random Pick Index
    - Implement RandM() using RandN()
        - 470-Implement Rand10() Using Rand7()
    - others:
        - eg: 528-Random Pick with Weight (with prefix-sum); 497-Random Point in Non-overlapping Rectangles (with binary search)
- Convex Hull:
    - algorithms: Jarvis Algorithm, Graham Scan, Monotone Chain
    - eg: 587-Erect the Fence

## Pre-computing:
- problems:
    - Calculation with certain restrictions: precompute partial results
        - eg: 238-Product of Array Except Self
    - Saving compute time
        - eg: 303-Range Sum Query - Immutable

## Prefix sum:
- key words: sum of subarray 
usually solved with O(n) time using hashmap - eg.303-Range Sum Query - Immutable; 560-Subarray Sum Equals K,325-Maximum Size Subarray Sum Equals k; 930,974|1590(division),1371,1442,437(tree version), 1124, 528-Random Pick with Weight

## Priority Queue:
- key words: sort
- problems:
    - sorting:
        - eg: 23-Merge k Sorted Lists; 778-Swim in Rising Water
    - greedy:
        - eg: 1353-Maximum Number of Events That Can Be Attended; 502-IPO, 630-Course Schedule III(greedy * 2)|1383-Maximum Performance of a Team; 1851-Minimum Interval to Include Each Query

## Sliding window -
- variations:
    - fixed length sliding window:
        - eg. 1052
    - substring that has given numbers of certain characters: 
        - algorithm: move right pointer to right until satisfies condition, then move left pointer to right to tighten window until condition not satisfied
        - eg. 3-Longest Substring Without Repeating Characters | 159-Longest Substring with At Most Two Distinct Characters | 340. Longest Substring with At Most K Distinct Characters | 992-Subarrays with K Different Integers | 395. Longest Substring with At Least K Repeating Characters; 76,1234; similar:904;1004-Max Consecutive Ones III;1358-Number of Substrings Containing All Three Characters;
    - subarray sum with a target: sliding window with prefix-sum / two pointers
        - eg: 209,930,1658
- tips:
    - can use monotonically decreasing queue to keep track of the max/min in window. Suitable for when the window size is large. eg.239,1696

## Sorting
- quick sort 
    - algorithm:
        1. find a random pivot
        2. put the pivot in its sorted position (elements to its left are smaller and elements to its right are greater)
        3. recursively sort the left and the right partition
    - Complexity:
        O(nlogn) on average; O(n^2) worst case
        O(1) space (in-place sorting)
    - variations:
        quick select: eg.215, 973 O(n) on average since only sorting one partition; O(n^2) worst case
- merge sort: 
    - algorithm:
        1. recursively call merge_sort on left half, then on right half
        2. merge left half and right half
    - Complexity:
        time: O(nlogn)
        space: O(n) - number of nodes in the recursion tree
    - Examples: 315(hard)
- *sort an almost sorted array where two elements are swapped
    - Examples: 99
- wiggle sort
    - Example: 280
- bucket sort
    - eg. 164
- custom sort
    - eg: 179-Largest_Number

## Stack
- classic problems:
    - straight forward stack:
        - eg: 636-Exclusive Time of Functions
    - parenthesis: 
        - eg. 32, 678, 856, 1249, 1541
        - can also use two passes: 32
    - monotonically increasing/decreasing stack
        - comparison:
            - eg: 496,503-Next Greater Element I/II; 1063-Number of Valid Subarrays; 739-Daily Temperatures; 901-Online Stock Span; 456-132 Pattern; 1019-Next Greater Node In Linked List, 1130-Minimum Cost Tree From Leaf Values; 
        - smallest/largest number formed by subsequence:
            -eg. 1673-Find the Most Competitive Subsequence; 402-Remove K Digits
        - window max/min (with monotonically increasing/decreasing stack)
            - intuition: it is very useful to get "next bigger item", "next smaller item", "previous bigger item", "previous smaller item" and therefore "window max" and "window min"
            - eg: 84-Largest Rectangle in Histogram; 907-Sum of Subarray Minimums; 1856-Maximum Subarray Min-Product(similar:907); 962-Maximum Width Ramp; 1124-Longest Well-Performing Interval
            

## String manipulation:
use reversed string to avoid index shift (833)

## Sweep Lines:
- Key words:
intervals
- Clarification Questions: 
Q: Are intervals mutually exclusive? A: Yes
- Algorithm pattern: 
    - Sort and scan 
    - priority queue/greedy  
- Data structures:
- Complexity:
O(n), O(n)
- Variations: 
    - streaming intervals (can usually solve using bisect), eg 729, 731, 732, 57
    - greedy with priority queue: 1353-Maximum Number of Events That Can Be Attended; 1834-Single-Threaded CPU
- Examples:
eg: 56, 57, 218, 252, 253, 435, 452, 986-Interval List Intersections, 1229-Meeting Scheduler, 1272, 1288, Lint391; hard-352, 391(2D), 759, 850(2D)

## Sums:
- Key words: 2 sum, 3 sum equal/smaller/closest to the target
- eg: 1, 167, 15, 259
- tips:
    hashmap or two-pointers
- variations:
    - running counter (with hashmap): 
        - key words: number of ways to get target sum/product
        - eg: 1577-Number of Ways Where Square of Number Is Equal to Product of Two Numbers

## Topological Sort:
    - eg: 207-Course Schedule | 210. Course Schedule II; 444-Sequence Reconstruction

### Two pointers:
- classic problems:
    - palindrom: 680
    - two arrays: 1537-Get the Maximum Score; 1868-Product of Two Run-Length Encoded Arrays

## Tree - Recursion can usually be used. 
If using dfs, has to decide which to use: in-order traversal (aka. dfs), post-order traversal (549,1740), and pre-order traversal (298, search tree). Time complexity is O(n): every node is visited once. Space complexity is O(n) in worst case and O(log(n)) in average case: The extra space comes from implicit stack space due to recursion. For a skewed binary tree, the recursion could go up to n levels deep. 
If using bfs, usually uses a FIFO queue to store nodes to be visited. 

## Trie
- when to use: Trie could use less space compared to hashmap when storing many keys with the same prefix (word search, spell checker, etc.)
- Trie data structure
```
class TrieNode:
    def __init__(self):
        self.isWord = False # mark word end
        self.children = collections.defaultdict(TrieNode)
```
- eg: 211-Design Add and Search Words Data Structure(basic)

## Union Find
- algorithm: union find by rank (assign node with higher rank as parent of a connected group)
- problem:
    - find connected groups: 323-Number of Connected Components in an Undirected Graph; 803-Bricks Falling When Hit (hard)
    - operation chaining: 399-Evaluate Division
