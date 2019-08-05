two sum: 1, 167


all, any: 833
array: 54,56,73,151,186,238,268,349,350,849
backtracking: 17
bfs: 103,127,297,200,207,210,212
binary search:  222
bit manipulation: 268
bucket:299
dfs: 17,113,124,129,200,207,210,212,236,261,297,753,947
dynamic programming: 5,10,39,72,139
greedy: 45,135
hashmap: 1,76,138,159,299,895
heap: 23
inorder: 105,
linked list: 2,21,86,138,146,445
map: 205
math: 268,794
preorder: 105,545
recursive: 2,273
sort: 56
stack: 20,402
string: 151,165,833,929
topological sort: 210
tree: 222
trie: 208,212,212
two pointers: 42,76,86,121,159,167,904
union find: 323,947
zip: 833


bfs - key word: shorted path; elements: queue, visited; steps: while q, if q popped is target, finish, if not, add popped item's neighbors to the q; optimization: visited can be eliminated if allowed to change memory (mark on original data)

dynamic programming -
backtracking with memoization; steps: build dp memory, define what dp[i] represents, find update function(s)

String manipulation:
use reversed string to avoid index shift (833)