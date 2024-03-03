class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # can use heap to get min value (nums contains positive integers)
        heapq.heapify(nums)
        
        res = 0 # number of operations
        
        while len(nums) > 0 and nums[0] < k:
            # remove 2 smallest integers x and y
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            # add to array
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            res += 1
            
        return res
    