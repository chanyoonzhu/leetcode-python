"""
- Array
- O(n), O(n)
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        while i < len(asteroids):
            cur = asteroids[i]
            if i == 0 or cur > 0 or asteroids[i - 1] < 0: i += 1
            else:    
                if abs(asteroids[i - 1]) < abs(cur):
                    asteroids[i - 1] = cur
                    i -= 1
                elif asteroids[i - 1] == abs(cur):
                    del asteroids[i - 1]
                    i -= 1
                del asteroids[i]
        return asteroids

"""
- Stack
- O(n), O(n)
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            if num > 0:
                stack.append(num)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -num:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(num)
                elif stack[-1] == -num:
                    stack.pop()
        return stack