# class Solution:
#     def tribonacci(self, n: int) -> int:
# #         DP - Tabulation, iteratively calc bottom up
#         t = {}
#         t[0] = 0
#         t[1] = 1
#         t[2] = 1
#         if n in t:
#             return t[n]
        
#         for i in range(3, n + 1):
#             t[i] = t[i-1] + t[i-2] + t[i-3]
            
#         return t[n]

# DP - memoization
class Solution:
    def tribonacci(self, n: int) -> int:
        t = [-1 for i in range(n + 1)]
        
        def cache(x, t):
            if x == 0:
                return 0
            if x == 1:
                return 1
            if x == 2:
                return 1
            if t[x] != -1: # solution found
                return t[x]
            # otherwise, calculate t[x] = t[x-1] + t[x-2] + t[x-3] recursively
            t[x] = cache(x-1, t) + cache(x-2, t) +  cache(x-3, t)
            return t[x]
        
        return cache(n, t)