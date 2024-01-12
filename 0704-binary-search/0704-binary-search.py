class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        l,r = 0, len(nums) - 1
        # (m)
            
        while l <= r:
            m = (l + r) // 2
            # to prevent overflow (cannot add 2 big numbers in other languages):
            # add l to the mid distance of r and l
            # m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1
    
    # def binarySearch(nums, left, right, target):
    #     while 
        