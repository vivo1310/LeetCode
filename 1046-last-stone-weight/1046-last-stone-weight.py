class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # if len(stones) == 1: return stones[0]
        # max heap, take out 2 largest stones, get the diff, push back to heap
        # https://docs.python.org/3/library/heapq.html
        
        data = [-x for x in stones] # trick to get max heap
        
        heapq.heapify(data) # O(n)
        
        while len(data) > 1:            
            diff = heapq.heappop(data) - heapq.heappop(data)
            heapq.heappush(data, diff)
            # heapq.heapify(data)
            
        return -data[0]
            
        
        