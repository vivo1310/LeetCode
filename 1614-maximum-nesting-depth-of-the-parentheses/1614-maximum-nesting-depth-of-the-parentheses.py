class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        depth = 0
        stack = []
        
        for c in s:
            if c == "(":
                stack.append(c)
                depth += 1
                
            elif c == ")":
                stack.pop()
                depth -= 1
            maxDepth = max(depth, maxDepth)
        return maxDepth