class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i, j = 0, 1
        res = []
        
        while i < len(prices) - 1 and j < len(prices):
            if prices[j] <= prices[i]:
                res.append(prices[i] - prices[j])
                i += 1
                j = i + 1
            elif j == len(prices) - 1:
                res.append(prices[i])
                i += 1
                j = i + 1
            else:
                j += 1
            if i == len(prices) - 1:
                res.append(prices[i])
        return res