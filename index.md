two sum: 1, 167


all, any: 833
array: 54,56,73,151,186,238,268,349,350,849
backtracking: 17
bfs: 79,103,116,127,133,297,200,207,210,212,529
binary search:33,222,240
bit manipulation: 268
bucket:299
dfs: 17,79,113,124,129,133,200,207,210,212,236,261,297,529,695,753,947
dynamic programming: 5,10,39,70,72,139,303,746,1314
greedy: 45,53,135
hashmap: 1,76,138,159,169,229,299,392,895
heap: 23,218
inorder: 105,
linked list: 2,21,24,25,86,138,146,445
map: 205
math:168,268,794,836
misc:169,229(moore voting)
preorder: 105,545
queue:232
range sum: 1314
recursive: 2,116,273,450
sort: 56
stack: 20,232,402
string: 151,165,722,833,929
topological sort: 210
tree: 116,222,450
trie: 208,212,212
two pointers: 42,76,86,121,159,167,392,904
union find: 323,947
zip: 833


bfs - key word: shorted path; elements: queue, visited; steps: while q, if q popped is target, finish, if not, add popped item's neighbors to the q; optimization: visited can be eliminated if allowed to change memory (mark on original data)

dfs - don't forget to reset visited back when all the branched dfs does not succeed.

dynamic programming -
backtracking with memoization; steps: build dp memory, define what dp[i] represents, find update function(s)

String manipulation:
use reversed string to avoid index shift (833)