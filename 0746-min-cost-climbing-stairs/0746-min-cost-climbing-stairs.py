class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        cost.append(0)
        n = len(cost)
        # cost = [10,15,20,0,0]
        # either 1 or 2 steps
        # dp[3] = min(dp[3] + dp[4], dp[3] + dp[5])
        # dp[2] = min(dp[2] + dp[3], dp[2] + dp[4])
        for i in range(n - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
        # print(cost)
        return min(cost[:2]) # as we can start at either index 0 or 1