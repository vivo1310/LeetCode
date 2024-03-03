class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # find number in nums that are less than k
        
        count = 0
        for n in nums:
            if n >= k:
                count += 1
        return len(nums) - count