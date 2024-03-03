class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # can use heap to get min value (nums contains positive integers)
        heapq.heapify(nums)
        print(nums)
        
        res = 0
        
        # remove 2 smallest integers x and y
        
        while len(nums) > 0 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            res += 1
        return res
    