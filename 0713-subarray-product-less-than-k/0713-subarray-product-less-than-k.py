class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0 # edege case
        prod = 1
        count = 0
        
        i = 0
        
        for j, num in enumerate(nums):
            prod *= num
            while prod >= k: 
                prod //= nums[i]
                i += 1
            count += j - i + 1
        return count

# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        