class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for x in nums:
            x = abs(x)
            if nums[x-1] < 0:
                return x
            nums[x-1] *= -1 # mark visited
        return -1
#         for i in range(len(nums)):
#             ind = abs(nums[i])
#             if nums[ind] < 0:
#                 return ind
#             nums[ind] = -nums[ind]
#         return -1