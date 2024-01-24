# DP - tabulation
# Bottom-up approach
# Stores the results of subproblems in a table
# Iterative implementation

# Well-suited for problems with a large set of inputs
# Used when the subproblems do not overlap
# Here’s an example of using memoization and tabulation to solve the same problem – calculating the nth number in the Fibonacci sequence:
# class Solution:
#     def fib(self, n: int) -> int:
#         f = {}
#         f[0] = 0
#         f[1] = 1
#         if n in f:
#             return f[n]
#         for i in range(2, n + 1):
#             f[i] = f[i-1] + f[i-2]
#         return f[n]
    
# DP - memoization
# Top-down approach
# Caches the results of function calls
# Recursive implementation
# Well-suited for problems with a relatively small set of inputs
# Used when the subproblems have overlapping subproblems
class Solution:
    def fib(self, n: int) -> int:
#         to find f[n], find f[n-1], f[n-2]
        memo = [-1 for i in range(n + 1)]
        
        def cacheFib(x, memo):
            if x == 0:
                return 0
            if x == 1:
                return 1
            if memo[x] != -1: # solution found
                return memo[x]
            # otherwise, store f[x] = f[x-1] + f[x-2]
            memo[x] = cacheFib(x-1, memo) + cacheFib(x-2, memo)
            
            return memo[x]
        
        return cacheFib(n, memo)