class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        l = 0
        r = 1
        maxP = 0
        while r < len(prices):
            currP = prices[r] - prices[l]
            if prices[l] < prices[r]:
                maxP = max(maxP, currP)
                # we're buy at low, sell at high, keep L, move R forward
                r += 1
            else:
                # we're at buy high, sell low, not good, replace L with R, move R 1 point forward from new L
                l = r
                r = l + 1
        return maxP if maxP > 0 else 0