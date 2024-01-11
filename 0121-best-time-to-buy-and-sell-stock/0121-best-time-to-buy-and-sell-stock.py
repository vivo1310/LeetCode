class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        l = 0
        r = 1
        maxP = prices[r] - prices[l]
        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
                # we're buy at low, sell at high, keep L, move R forward
                r += 1
            else:
                # we're at buy high, sell low, not good, replace L with R, move R 1 point forward from new L
                l = r
                r = l + 1
        return maxP if maxP > 0 else 0