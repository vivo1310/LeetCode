class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # if len(stones) == 1: return stones[0]
        # max heap, take out 2 largest stones, get the diff, push back to heap
        
        data = [-x for x in stones]
        
        heapq.heapify(data) # to get max heap
        
        print(data)
        while len(data) > 1:
            diff = heapq.heappop(data) - heapq.heappop(data)
            heapq.heappush(data, diff)
            heapq.heapify(data)
            
        print(data)
        return -data[0]
            
        
        