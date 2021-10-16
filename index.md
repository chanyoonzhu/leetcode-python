two sum: 1, 167


all, any: 833
array: 54,56,68,73,122,151,157,186,238,268,349,350,380,381,849,1146,1371,1381,1526,1567,1706
backtracking: 17,46,47,78,90,301,491,698,996,1088,1593,1239,1307,1681,1718,1723,1774
bfs: 79,103,116,126,127,133,200,207,210,212,269,279,297,301,399,407,444,505,529,542,743,752,785,787,803,863,919,934,959,971,987,1110,1236,1254,1293,1306,1345,1654,1778
binary search:4,29,33,34,57,81,153,154,162,222,240,259,268,275,279,287,295,300,374,410,715,774,875,911,1011,1055,1146,1231,1272,1283,1428,1482,1552,1608,1648,1723,1802,1870
bitwise operation: 29,136,137,191,231,268,318,338,342,371,461,473,476,491,693,698,1284,1371,1442,1542,1593,1681
binary search tree: 99,230,333,449,450,490,729,1008
bucket:299
circular array: 213,1658
divide and conquer: 53,215,241,307,308,312,327,395,973,1000,1039,1547
dfs: 17,79,91,99,105,106,113,124,129,133,200,207,210,212,230,236,241,261,297,298,301,329,331,333,337,394,399,449,490,529,543,549,652,666,687,690,694,695,743,753,778,785,787,803,863,889,934,947,951,959,975,987,1028,1110,1236,1306,1340,1462,1569,1644,1676,1740,1766,1778
dynamic programming: 5,10,32,39,45,53,55,64,70,72,91,97,115,139,188,198,213,221,256,265,276,279,300,312,322,375,403,410,413,416,435,464,473,474,486,494,516,518,542,552,562,583,634,712,727,740,746,805,813,837,877,879,920,931,940,956,1000,1035,1039,1048,1092,1105,1140,1143,1155,1216,1269,1277,1278,1312,1314,1335,1406,1458,1510,1547,1548,1696,1746,1774,1824,1937,1981
graph: 785,863
greedy: 45,53,55,135,410,435,455,621,630,678,774,785,843,853,875,877,1011,1231,1353,1383,1402,1419,1428,1482,1520,1537,1552,1567,1648,1665,1718,1746,1775,1802,1824,1851,1870
hashmap: 1,15,76,106,138,146,149,159,169,229,246,299,327,336,340,359,380,381,392,398,403,432,437,465,496,560,666,792,895,930,974,1000,1055,1371,1442,1525,1542,1577,1590,1644
hashset: 1,381,432,694,1239,1452,1774
inorder: 99,105,230,333,426
linked list: 2,21,24,25,86,138,146,382,432,445,587,705,706,1650
logic deduction: 444 
map: 205
math:12,149,168,268,279,391,470,621,794,836,837,952,1041,1344,1569,1610,1627,1998
merge sort: 315,1574
misc:169,229(moore voting)
preorder: 105,106,113,331,437,449,545,652,666,889,971,987,1008,1028,1569
priority queue: 23,215,218,239,253,295,347,373,404,621,630,632,759,778,973,1229,1353,1383,1438,1439,1499,1675,1696,1834,1851,1882
queue:232,239,656,1438,1499,1696
range sum: 307,308,327,1314,930,1442
recursive: 2,116,241,247,273,450,772,1106
segment tree: 307,308,327,850
sliding window: 3,76,159,209,239,340,395,837,862,904,930,992,1004,1052,1234,1358,1371,1423,1498,1509,1537,1574,1577,1610,1658,1696,1793,1839
sort: 56,99,164,179,252,280,315,524,581,593,L391,1300,1509,1608,1610
stack: 20,32,42,71,84,155,224,227,232,331,394,402,456,496,503,581,636,678,735,739,772,856,901,907,946,962,975,1019,1028,1063,1106,1124,1130,1209,1249,1381,1541,1597,1673,1776,1856
string: 151,157,165,418,722,833,929,1520
topological sort: 207,210,269,329,444.1462
tree: 116,222,235,236,298,333,337,426,450,543,549,652,687,729,919,1644,1650,1676,1740
trie: 208,211,212,336
two pointers: 15,42,76,86,121,159,167,209,246,253,259,392,524,581,680,904,986,1055,1229,1248,1537,1574,1577,1658,1775,1868
union find: 128,305,323,778,947,952,1562,1627,1722,1970,1998
zip: 833


## Array
- Problems:
    - print screen: 68-Text Justification; 418-Sentence Screen Fitting
    - 1D array: 1562-Find Latest Group of Size M(hard)
    - 2D array: 1706-Where Will the Ball Fall

## backtracking 
    - eg: 17-Letter Combinations of a Phone Number; 78-Subsets(classic)|90-Subsets II|46-Permutations|47-Permutations II; 491-Increasing Subsequences; 996-Number of Squareful Arrays; 1239-Maximum Length of a Concatenated String with Unique Characters; 698-Partition to K Equal Sum Subsets; 1088-Confusing Number II; 1593-Split a String Into the Max Number of Unique Substrings; 1681-Minimum Incompatibility; 1307-Verbal Arithmetic Puzzle(hard); 1718-Construct the Lexicographically Largest Valid Sequence (with greedy); 1723-Find Minimum Time to Finish All Jobs(hard, with binary search); 1774-Closest Dessert Cost；465-Optimal Account Balancing (hard)

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
- Examples: 57,911,1146(bisect), 278,374-Guess Number Higher or Lower(basic), 981(strictly increasing, find lower), 315
- problems:
    - binary search the answer: get the possible range of answer, binary search between range and see if current number can satisfy condition using greedy algorithm
        - eg: 287-Find the Duplicate Number; 410-Split Array Largest Sum|774; 778-Swim in Rising Water(graph)|875|1011|1231|1283|1300|1482|1552|1648|1802(complex)|1870;1723-Find Minimum Time to Finish All Jobs(hard, with backtracking); 279-Perfect Squares
    - multiplication/division: 29-Divide Two Integers
    - arrays: 
        - find target:
            eg. 34-Find First and Last Position of Element in Sorted Array; 162-Find Peak Element (unsorted)
        - rotated arrays:
            - tip: when there are duplicates, add duplicates removal steps (154, 81)
            - eg. 153-Find Minimum in Rotated Sorted Array|154. Find Minimum in Rotated Sorted Array II|33-Search in Rotated Sorted Array|81-Search in Rotated Sorted Array II; 
        - merge arrays:
            - eg. 4-Median of Two Sorted Arrays

## Bitwise Operation
- AND
    - tricks:
        - x & 1: get the rightmost bit
        - x & (x - 1): remove rightmost 1
    - eg. 190-Reverse Bits; 191-Number of 1 Bits; 231-Power of Two; 342-Power of Four; 338-Counting Bits
- XOR
    - definition - same: 0, different: 1
    - problems:
        - a number XOR itself equals 0: 136-Single Number; 137-Single Number II; 268-Missing Number
        - Subarray containing chars with certain conditions
            - tips: memoize the state of all prefixes in a hashmap, compute state using XOR
            - eg: 1371(even/odd),1542
        - Pure XOR: 1442,
        - Addition: 371-Sum of Two Integers
        - Bit difference/similarity: 461-Hamming Distance; 693-Binary Number with Alternating Bits
        - flip the bit: 476-Number Complement
- Bit shift
    - multiplication: 29-Divide Two Integers


## Bit-masking
- problems:
    - compression/serialization:
        - eg: 287-Find the Duplicate Number; 318-Maximum Product of Word Lengths; 1284-Minimum Number of Flips to Convert Binary Matrix to Zero Matrix (bfs)
    - enumeration (can be solved using backtracking):
        - eg: 90-Subsets II; 491-Increasing Subsequences; 698-Partition to K Equal Sum Subsets; 1593-Split a String Into the Max Number of Unique Substrings; 1681-Minimum Incompatibility

## BFS
- key word: shorted path (eg. 1345); 
- algorithm:
    elements: queue, visited hashset; 
    steps: while q, if q popped is target, finish, if not, add popped item's neighbors to the q; optimization: visited can be eliminated if allowed to change memory (mark on original data)
- problems:
    - all shortest paths: 301
    - 1D (array): 1654-Minimum Jumps to Reach Home; 279-Perfect Squares
    - 2D shortest paths: 505-The Maze II;542-01 Matrix; 1284-Minimum Number of Flips to Convert Binary Matrix to Zero Matrix (hard); 1293-Shortest Path in a Grid with Obstacles Elimination (hard)
    - String: 752-Open the Lock
    - Dijkstra's Algorithm:
        - key words: minimal cost of paths (unlike regular shortest path where cost is always 1, each connection can have various cost)
        - intuition: similar as bfs, difference is that instead of using a queue and always pop left (which is by default the minimal cost), use a heap to store tuple (total_cost, node) to always pop the smallest cost; also need an array/map to memoize smallest cost to each node
        - eg. 743-Network Delay Time (classic); 505-The Maze II; 787-Cheapest Flights Within K Stops; 407-Trapping Rain Water II (implicit); 656-Coin Path(hard, TLE)
    - tree traversal: see "## Tree"
    - construct sequence with topological sort (see "## Topological Sort")
    - bidrectional dfs
        - purpose: speeding up bfs
        - patterns: use two sets to store current nodes visited from beginning and end layers; for each round of bfs, search from the set with fewer nodes
        - 127-Word Ladder|126-Word Ladder II(hard); 1345-Jump Game IV
    - not only min distance, but need routes with min distance:
        - eg: 126-Word Ladder II

## Cache
- tip: cache previous result to save time
- eg: 418-Sentence Screen Fitting

## Counter
    eg: 900-RLE Iterator; 1419-Minimum Number of Frogs Croaking

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
- example: 230, 337; 690-Employee Importance; 778-Swim in Rising Water

## 2D DFS/BFS
- problems:
    - map hidden graph
        - eg: 1778-Shortest Path in a Hidden Grid; 1810-Minimum Path Cost in a Hidden Grid
    - find contiguous "islands"
        - eg: 200-Number of Islands | 694-Number of Distinct Islands | 1254-Number of Closed Islands | 934-Shortest Bridge (bfs + dfs); 959-Regions Cut By Slashes (need pixelating); 803-Bricks Falling When Hit (hard)
    - operation chaining:
        - eg: 399-Evaluate Division
    - other: 1766-Tree of Coprimes (hard)

## Dynamic programming -
backtracking with memoization; steps: build dp memory, define what dp[i] represents, find update function(s)
space can be optimized to O(1) if only need to track constant time of variables for each update
- Top down (depth-first-search): recursion using memoization
- Bottom up: loop using memoization (calculate those won't change first, eg.1143, 1340) - look at the transformation formula from the top-down solution to figure out what needs to be calculated first in the loop. Can use the subproblem size as the outer loop if dp(i, j) need dp(i + 1, j - 1) (eg.312，375, 486, 877, 1312)
- problems:
    - dp[i] depends on dp[i-1]: 
        - eg.70-Climbing Stairs; 198-House Robber|213. House Robber II||740-Delete and Earn; 256-Paint House|265-Paint House II; 276-Paint Fence(a hard medium); 413-Arithmetic Slices; 91-Decode Ways;139-Word Break; 837-New 21 Game; 940-Distinct Subsequences II
    - dp[i] depends on dp[j] where j in [1...i]:
        - eg. 64-Minimum Path Sum; 542-01 Matrix; 221-Maximal Square | 1277-Count Square Submatrices with All Ones; 931-Minimum Falling Path Sum | 1937-Maximum Number of Points with Cost; (revisit above examples!) 940. Distinct Subsequences II; 1105-Filling Bookcase Shelves
    - dp[i][j] depends on dp[i+1][j-1]:
        - tip: use subproblem size (diff between i and j) as the outer loop
        - eg: 312-Burst Balloons(hard)，375-Guess Number Higher or Lower II; 486, 516-Longest Palindromic Subsequence, 877, 1312
    - intervals: sequence needs to be divided into k distinct intervals
        - key words: split array
        - dp[i][k] depends on dp[j][k-1] where j = [1...i]
        - eg: 410-Split Array Largest Sum; 813-Largest Sum of Averages; 1278-Palindrome Partitioning III; 1335-Minimum Difficulty of a Job Schedule
    - two sequences:
        - key words: longeest common subsequences, shortest common superseequence, edit distance, ...
        - tip: dp[i][j] result at s1[:i1+1] and s2[:i2+1]
        - eg.
            - longeest common subsequences/shortest common superseequence: 97-Interleaving String; 115-Distinct Subsequences; 727. Minimum Window Subsequence; 1143-Longest Common Subsequence; 1092-Shortest Common Supersequence
            - edit distance: 72-Edit Distance; 583-Delete Operation for Two Strings|712. Minimum ASCII Delete Sum for Two Strings; 1216-Valid Palindrome III|1312. Minimum Insertion Steps to Make a String Palindrome; 1548-The Most Similar Path in a Graph
            - palindrome: 516-Longest Palindromic Subsequence, 1216-Valid Palindrome III|1312. Minimum Insertion Steps to Make a String Palindrome
        - advanced: ask to track path
            - tip: can store min/max in dp first, then trace the path
            - eg: 727-Minimum Window Subsequence; 1092-Shortest Common Supersequence
    - knapsack: 
        - keyword: combine numbers in array to reach a target
        - memo: dp[_sum][i]
        - tip: for 0/1 knapsack: decrease i to avoid over counting; for 0/n knapsack: increase i to allow counting more than 1 time
        - problems:
            - 0/1 knapsack: each element can be used 0 or 1 time
                - eg: 416-Partition Equal Subset Sum|956-Tallest Billboard(hard, need max);474-Ones and Zeroes(two bags);1981-Minimize the Difference Between Target and Chosen Elements;805-Split Array With Same Average;879-Profitable Schemes(hard 3D);
            - 0/n knapsack: each element can be used 0 or infinite amount of times
                - eg: 322-Coin Change; 1449-Form Largest Integer With Digits That Add up to Target
            - pos/neg knapsack: 494-Target Sum;1049-Last Stone Weight II
        - eg: 630-Course Schedule III; 1774-Closest Dessert Cost
    - length in matrix: 562
    - reachable problem: 45,55
    - merge: divide and conquer: 241
        - calculation among adjacent items: 312, 1039, 1547, 1000-Minimum Cost to Merge Stones(hard)
            - tip: when bottom-up, use subproblem size as the outer loop
    - game theory: 375. Guess Number Higher or Lower II; 486-Predict the Winner|877-Stone Game|1140-Stone Game II|1406-Stone Game III|1510-Stone Game IV
    - string subsequence with min/max cost: 97,516,583,1035,1092,1143,1458
        - edit-distance: 72,583,712,1312,1548-The Most Similar Path in a Graph
        - subsequence combinations: 115-Distinct Subsequences
    - string/serialized list or set as memoization key: 464-Can I Win; 1048-Longest String Chain
    - number of ways:
        - tip: can use dp[i] to store number of ways when ending at element i, then the result is sum(dp) (eg.940)
        - eg: 115-Distinct Subsequences; 1155-Number of Dice Rolls With Target Sum; 279-Perfect Squares; 1269-Number of Ways to Stay in the Same Place After Some Steps; 276-Paint Fence(a hard medium); 552-Student Attendance Record II(hard); 940-Distinct Subsequences II (hard)
        - combination/permutation: 
            - tip: 分类讨论
            - 634-Find the Derangement of An Array(hard); 920-Number of Music Playlists(hard)
    - subarray max/min: 
        - can also use greedy
        - eg: 53-Maximum Subarray; 1746-Maximum Subarray Sum After One Operation
    - subsequence:
        - eg: 300-Longest Increasing Subsequence
    - others:
        - eg: 188-Best Time to Buy and Sell Stock IV      

## Graph
- Complexity
    - time: O(N + E) N - number of nodes; E: number of edges
    - space: O(N)
- Algorithms: DFS and BFS
- Problems:
    - eg: 785-Is Graph Bipartite?
    - minimum cost path: Dijkstra Algorithm (see "## BFS")

## Greedy -
- instinct: 
Pick the locally optimal move at each step, and that will lead to the globally optimal solution.
Iterate over the array and update at each step the standard set for such problems: 1.current element 2.current local maximum sum (at this given point) 3.global maximum sum seen so far.
    - eg: 1402,1520,1665
- problems:
    - greedy with sort: 853-Car Fleet; 1775-Equal Sum Arrays With Minimum Number of Operations; 1537-Get the Maximum Score
    - maximum subarray: 53-Maximum Subarray; 1746. Maximum Subarray Sum After One Operation
    - minimum state change: 1824-Minimum Sideway Jumps
    - game theory: 464-Can I Win; 486-Predict the Winner; 843-Guess the Word; 877-Stone Game | 1140-Stone Game II|1406-Stone Game III|1510-Stone Game IV

## Hashset
- problems:
    - set operation: 1452-People Whose List of Favorite Companies Is Not a Subset of Another List
    - Storing states: 1774-Closest Dessert Cost

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
    - eg. 268-Missing Number; 1648, 1802
- Sampling:
    - reservoir sampling: sampling in large/dynamic-size arrays with O(1) space
        - eg: 382-Linked List Random Node; 398-Random Pick Index
    - Implement RandM() using RandN()
        - 470-Implement Rand10() Using Rand7()
    - sampling with weight:
        - algorithm: prefix-sum with binary search
        - eg: 528-Random Pick with Weight (with prefix-sum); 497-Random Point in Non-overlapping Rectangles (with binary search)
- Convex Hull:
    - algorithms: Jarvis Algorithm, Graham Scan, Monotone Chain
    - eg: 587-Erect the Fence
- Math deduction:
    - eg. 877-Stone Game
- Bachet's conjecture:
    - eg: 279-Perfect Squares
- Probability:
    - eg: 837-New 21 Game
- Factorization:
    - eg: 952-Largest Component Size by Common Factor; 1998-GCD Sort of an Array
- Primes:
    - eg: 1627-Graph Connectivity With Threshold; 1998-GCD Sort of an Array(Sieve of Eratosthenes)
- Trignometry:
    - radian
        - def: radians (0 degree - 0, 90 - 1.57, 180 - pi, 270 - -1.57, 360 - 0); radian of a line (defined by two points (a, b)) to positive x axis: math.atan2(b[1] - a[1], b[0] - a[0])
        - eg: 1610-Maximum Number of Visible Points

## Pre-computing:
- problems:
    - Calculation with certain restrictions: precompute partial results
        - eg: 238-Product of Array Except Self
    - Saving compute time
        - eg: 303-Range Sum Query - Immutable

## Prefix sum:
- key words: sum of subarray 
- tip: usually solved with O(n) time using hashmap 
- eg.303-Range Sum Query - Immutable; 560-Subarray Sum Equals K,325-Maximum Size Subarray Sum Equals k; 930,974|1590(division),1371-Find the Longest Substring Containing Vowels in Even Counts;1442,437(tree version), 1124, 528-Random Pick with Weight; 1248-Count Number of Nice Subarrays1525-Number of Good Ways to Split a String

## Priority Queue (Heap):
- tip: stores tuples in queues, a tuple is comprised of number (a group of numbers) needs to be sorted and the information need to pass when that number is popped from the heap
- key words: sort
- problems:
    - queue with conditions: 1882-Process Tasks Using Servers
    - sorting:
        - eg: 23-Merge k Sorted Lists; 373-Find K Pairs with Smallest Sums|1439-Find the Kth Smallest Sum of a Matrix With Sorted Rows; 632-Smallest Range Covering Elements from K Lists; 778-Swim in Rising Water; 1675-Minimize Deviation in Array
    - greedy:
        - eg: 1353-Maximum Number of Events That Can Be Attended; 502-IPO, 630-Course Schedule III(greedy * 2)|1383-Maximum Performance of a Team; 1499-Max Value of Equation; 1851-Minimum Interval to Include Each Query; 
    - Dijkstra's Algorithm (see "## BFS")

## Sliding window -
- problems:
    - fixed length sliding window:
        - eg. 1052; 1509-Minimum Difference Between Largest and Smallest Value in Three Moves
    - substring that has given numbers of certain characters: 
        - algorithm: move right pointer to right until satisfies condition, then move left pointer to right to tighten window until condition not satisfied
        - eg. 3-Longest Substring Without Repeating Characters | 159-Longest Substring with At Most Two Distinct Characters | 340. Longest Substring with At Most K Distinct Characters | 992-Subarrays with K Different Integers | 395. Longest Substring with At Least K Repeating Characters; 76,1234; similar:904;1004-Max Consecutive Ones III;1248-Count Number of Nice Subarrays (loose end); 1358-Number of Substrings Containing All Three Characters; 1371-Find the Longest Substring Containing Vowels in Even Counts; 1438-Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit;1839-Longest Substring Of All Vowels in Order; 1658-Minimum Operations to Reduce X to Zero
    - subarray sum with a target: sliding window with prefix-sum / two pointers
        - eg: 209,930,1658
    - use a sliding window to keep the running sum of last n items: 837-New 21 Game
    - largest size of subsequence with in target diff: 
        - tip: sort first
        - eg. 1610-Maximum Number of Visible Points(hard, 2D)
    - monotonic queue: 
        - intuition: keep track of the max/min in window when window size is large; can be more effiecient than the solution using a priority queue which has a complexity of O(nlogk) where k is the window size (eg.1499).
        - algorithm: 
            - after popleft() indexes out of range, q[0] is the next smallest/largest
            - after pop() indexes i with nums[i] >(<) nums[curr_i], append curr_i to q as next candidate.
        - complexity: O(n), O(n) - each item queued and popped exactly once
        - eg. 239-Sliding Window Maximum; 656. Coin Path(hard); 862-Shortest Subarray with Sum at Least K; 1438-Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit(two queues); 1499-Max Value of Equation; 1696-Jump Game VI

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
    - Example: 280-Wiggle Sort
- bucket sort
    - eg. 164
- custom sort
    - eg: 179-Largest_Number

## Stack
- problems:
    - straight forward stack:
        - eg: 071-Simplify_Path; 636-Exclusive Time of Functions; 735-Asteroid Collision; 1209-Remove All Adjacent Duplicates in String II
    - parenthesis: 
        - eg. 32, 394-Decode String; 678, 856, 1249, 1541; 772-Basic Calculator III
        - can also use two passes: 32
    - calculator:
        - tip: can use either a stack or a recursive solution
        - eg. 224-Basic Calculator|227-Basic Calculator II|772-Basic Calculator III; 1106-Parsing A Boolean Expression
    - monotonically increasing/decreasing stack
        - comparison:
            - eg: 496,503-Next Greater Element I/II; 1063-Number of Valid Subarrays; 739-Daily Temperatures; 901-Online Stock Span; 456-132 Pattern; 1019-Next Greater Node In Linked List, 1130-Minimum Cost Tree From Leaf Values; 
        - smallest/largest number formed by subsequence:
            -eg. 1673-Find the Most Competitive Subsequence; 402-Remove K Digits
        - window max/min (with monotonically increasing/decreasing stack)
            - intuition: it is very useful to get "next bigger item", "next smaller item", "previous bigger item", "previous smaller item" and therefore "window max" and "window min"
            - eg: 42-Trapping Rain Water; 84-Largest Rectangle in Histogram; 907-Sum of Subarray Minimums; 1856-Maximum Subarray Min-Product(similar:907); 962-Maximum Width Ramp; 1124-Longest Well-Performing Interval
        - collision: 1776-Car Fleet II
            

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
    - streaming intervals (can usually solve using bisect), eg: 715. Range Module; 729, 731, 732, 57
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
    - algorithm: 
        1. build node graph and increase indegrees
        2. add nodes with indegrees == 0 to queuq
        3. while q, pop node and bfs search neighbors of nodes, decrease their indegrees by 1, if indegree turns to 0, append to q
    - key words: construct sequence
    - eg: 207-Course Schedule | 210. Course Schedule II | 1462-Course Schedule IV; 444-Sequence Reconstruction; 269-Alien Dictionary(hard)

## Two pointers:
- problems:
    - palindrom: 680-Valid Palindrome II; 246-Strobogrammatic Number
    - two arrays: 1537-Get the Maximum Score; 1868-Product of Two Run-Length Encoded Arrays
    - sliding window (see "## sliding window")

## Tree - Recursion can usually be used. 
- If using dfs, has to decide which to use: in-order traversal (aka. dfs), post-order traversal (549,1740), and pre-order traversal (298, search tree). Time complexity is O(n): every node is visited once. Space complexity is O(n) in worst case and O(log(n)) in average case: The extra space comes from implicit stack space due to recursion. For a skewed binary tree, the recursion could go up to n levels deep. 
If using bfs, usually uses a FIFO queue to store nodes to be visited. 
- Problems:
    - pre-order: 297-Serialize and Deserialize Binary Tree; 449. Serialize and Deserialize BST; 951-Flip Equivalent Binary Trees; 1008-Construct Binary Search Tree from Preorder Traversal; 1110-Delete Nodes And Return Forest;
    - in-order traversal: 426-Convert Binary Search Tree to Sorted Doubly Linked List
    - post-order traversal: 543-Diameter of Binary Tree
    - traversal combinations: 105-Construct Binary Tree from Preorder and Inorder Traversal; 106-Construct Binary Tree from Inorder and Postorder Traversal; 889-Construct Binary Tree from Preorder and Postorder Traversal
    - BST(Binary Search Tree) Problems: 450-Delete Node in a BST; 1008-Construct Binary Search Tree from Preorder Traversal
    - Breath-first search(BFS): 
        - eg: 297-Serialize and Deserialize Binary Tree; 1110-Delete Nodes And Return Forest;
        - complete binary tree
            - eg: 919-Complete Binary Tree Inserter
    - Subtree hashing: 652-Find Duplicate Subtrees

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
- key word: connected group in a graph
- algorithm: union find by rank (assign node with higher rank as parent of a connected group)
```
parents = [i for i in range(n)]
        
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x]) # recursion
    return parents[x]

# simple version: when only need to find pair-wise connection (don't need a universal parent for all items in a connected part)
def union(x, y):
    px, py = find(x), find(y)
    if px != py: # connect parents of x, y
        parents[px] = py

# todo: full verion - assign parents by rank (guarantees that all connected items have the same parent)

def isXandYConnected(n):
    if shouldConnectXandY(x, y):
        union(x, y)
    
    return find(x) == find(y) # bubble up to parents

```
- problem:
    - find connected groups: 128-Longest Consecutive Sequence; 305-Number of Islands II(hard); 323-Number of Connected Components in an Undirected Graph; 803-Bricks Falling When Hit (hard); 1722-Minimize Hamming Distance After Swap Operations (implicit); 952-Largest Component Size by Common Factor; 1562-Find Latest Group of Size M(hard); 1627-Graph Connectivity With Threshold | 1970-Last Day Where You Can Still Cross; 1998-GCD Sort of an Array
    - operation chaining: 399-Evaluate Division

## Other
- Account Balance: 465-Optimal Account Balancing (hashmap + backtracking)

## Tricks
- bubble up dp mem array from side to middle
    - eg. 1937-Maximum Number of Points with Cost
