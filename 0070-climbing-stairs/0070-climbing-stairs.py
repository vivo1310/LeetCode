class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialise dp[0] = 1, as there is only one way for n = 0 and dp[1] = 2 as there are only 2 ways for input n = 2.
        dp = {}
        dp[0] = 1
        dp[1] = 2
        # 2 -> 3, 3 -> 5, 4 -> 8
        # print(n)
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
            # print(i,dp[i])
        # print(dp[n-1])
        return dp[n-1]