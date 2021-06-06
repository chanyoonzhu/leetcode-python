"""
- greedy, Gauss sum
- O(n), O(1)
- https://leetcode.com/problems/sell-diminishing-valued-colored-balls/discuss/927522/Python-n-log-n-690-ms
"""
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0)
        result, ind, max_color_counts = 0, 0, 0
        mod = 10 ** 9 + 7
        
        while orders > 0:
            max_color_counts += 1
            sell = min(orders, max_color_counts * (inventory[ind] - inventory[ind + 1]))
            all_sell_count, some_sell_count = divmod(sell, max_color_counts)
            result += max_color_counts * (all_sell_count * (inventory[ind] - all_sell_count + 1 + inventory[ind])) // 2 + some_sell_count * (inventory[ind] - all_sell_count)
            orders -= sell
            ind += 1
        return result % mod

"""
- binary search + greedy - todo
"""