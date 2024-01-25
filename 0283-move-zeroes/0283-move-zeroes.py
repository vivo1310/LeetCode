class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,0,0,3,12]
        left, right = 0, 0
        # findZero, findNonZeroToSwap0ToTheEnd
        while right < len(nums):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            right += 1
        
                
            
        
        
        
        