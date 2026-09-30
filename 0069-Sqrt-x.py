"""
- binary search
- O(logx), O(1)
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            mid_squared = mid ** 2
            if mid_squared == x:
                return mid
            elif mid_squared > x:
                hi = mid - 1
            else:
                lo = mid
        return lo



"""
- newton's method

Let's define: f(x) = x**2 - n
df(x) = 2 * x
a = df(x1) = 2 * x1
find b:
f(x1) = df(x1) * x1 + b
b = f(x1) - df(x1) * x1
so:
y = df(x1) * x + (f(x1) - df(x1) * x1)
Now we are looking for the intersection with the x-axis:
0 = df(x1) * x2 + (f(x1) - df(x1) * x1)
x2 = (df(x1) * x1 - f(x1))/df(x1)
x2 = x1  -  f(x1)/df(x1)
x2 = x1 - (x1**2 - n)/(2 * x1)
x2 = (2 * x1**2 - x1**2 + n)/(2 * x1)
x2 = (x1**2 + n)/(2 * x1)
x2 = (1/2) * (x1 + n/x1)
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        x_prev = x
        x_cur = x / 2
        precision = 0.1
        while abs(x_prev - x_cur) > precision:
            x_prev = x_cur
            x_cur = (1/2) * (x_cur + x/x_cur)
            
        return int(x_cur)
        