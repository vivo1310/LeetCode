# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # Initialise dp[0] = 1, as there is only one way for n = 0 and dp[1] = 2 as there are only 2 ways for input n = 2.
# #         DP - tabulation (bottom up)
#         dp = {}
#         dp[0] = 1
#         dp[1] = 2
#         for i in range(2, n):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[n-1]
    
    
#     DP - memoization (top down)
#   from n down to 0
        
    # Create a 1D dp where dp[i] represent the number of ways to reach the ith stair from the bottom.
    # Check if answer for subproblem already exist or not in dp.
    # Recursively call for subproblems and store their result in dp (i.e, dp[n] = countWays(n – 1, dp) + countWays(n – 2, dp)).
    # Finally, return dp[n], as it will store the answer for input n.

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n)]
        
        def climb(x, dp):
            if x == 0:
                return 1
            if x == 1:
                return 2
            if dp[x] != 0: # solution found at the top step
                return dp[x]
            
            dp[x] = climb(x-1, dp) + climb(x-2, dp)
            return dp[x]
        
        return climb(n - 1,dp)