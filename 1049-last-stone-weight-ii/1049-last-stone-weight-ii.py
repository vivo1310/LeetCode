class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # get the total sum of the stones' weights
        # [2,7,4,1,8,1] -> sum is 23 -> try to find if we can group stones so that the group's weight is 23/2 = 12 or 11
        # we should do this by divide the sum by half, because 12-11 will give us the smallest difference
        # if we have that group, we know that no matter how we smash the stone, we will end up getting the smallest weight of the left stone as the difference between the groups
        
        sumStones = sum(stones)
        target = ceil(sumStones / 2)
        
        cache = {} # (i, total)
        
        def dp(i = 0, total = 0):
            if total >= target or i == len(stones): # stop
                diff = abs(total - (sumStones - total))
                return diff
            if (i,total) in cache: # caching/memoization
                return cache[(i,total)]
            
            cache[(i,total)] = min(dp(i + 1, total), dp(i + 1, total + stones[i]))
            return cache[(i,total)]
        
        # dp()
        
        return dp()