class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = [] # min heap [smaller height, avg height, bigger height]
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            
            if diff > 0:
                heapq.heappush(pq, diff)
                if len(pq) > ladders:
                    bricks -= heapq.heappop(pq) # use bricks for small diff 
                if bricks < 0:
                    return i
                
        return len(heights) - 1
    
#         n = len(heights)
    
#         def dp(b=bricks, l=ladders, i=0):
#             if i >= n - 1:
#                 return i
            
#             diff = heights[i+1] - heights[i]
#             if diff > 0:
#                 ans = i
#                 if b >= diff:
#                     ans = max(ans, dp(b - diff, l, i + 1))
#                 if l > 0:
#                     ans = max(ans, dp(b, l - 1, i + 1))
#                 return ans
#             else:
#                 return dp(b, l, i + 1)
        
        
#         return dp()
    
    
        