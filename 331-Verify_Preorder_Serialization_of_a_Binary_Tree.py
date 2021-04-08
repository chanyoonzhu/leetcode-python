class Solution:

    """
    - dfs (preorder) with stack
    - O(n), O(n)
    - edge cases: "#" - true; "###" - false; "" - input invalid
    - intuition: all nodes need to be visited twice (from left and right child)
    """
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        stack = []
        if preorder[0] != "#":
            stack.append(0)
        for val in preorder[1:]:
            if not stack:
                    return False
            if val != "#":
                stack.append(0)
            else:
                stack[-1] += 1
                while stack and stack[-1] == 2:
                    stack.pop()
                    if stack:
                        stack[-1] += 1
        return not stack

    """
    - dfs (preorder) with stack - similar as previous solution
    - O(n), O(n)
    - edge cases: "#" - true; "###" - false; "" - input invalid
    - intuition: all nodes need to be visited twice (from left and right child)
    """
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        stack = [preorder[0]]
        collapse = ["#", "#"]
        for val in preorder[1:]:
            if not stack:
                    return False
            stack.append(val)
            while len(stack) >= 2 and stack[-2:] == collapse:
                stack.pop()
                stack.pop()
                if not stack or stack[-1] == "#":
                    return False
                else:
                    stack[-1] = "#"                
        return stack == ["#"]
    
    """
    - dfs (preorder) with a single variable
    - O(n), O(n)
    - intuition: all nodes need to be visited twice (from left and right child)
    """
    def isValidSerialization(self, preorder: str) -> bool:
        diff = 1
        for val in preorder.split(","):
            diff -= 1
            if diff < 0: return False # cannot have more "#" before there are enough non-"#" values to offset
            if val != "#": diff += 2 # need 2 "#" to offset
        
        return diff == 0