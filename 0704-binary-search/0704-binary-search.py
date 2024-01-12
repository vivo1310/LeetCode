class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums) == 1: return 0 if nums[0] == target else -1
        
        l,r = 0, len(nums) - 1
        m = (l + r) // 2
        # print(m)
            
        while l <= r:
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
            m = (l + r) // 2
            
        return -1
    
    # def binarySearch(nums, left, right, target):
    #     while 
        