class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # constraint 10^4 => aim for O(nlogn)
        nums.sort()
        
        for i in range(nums[-1]):
            if i != nums[i]:
                return i
        return nums[-1] + 1