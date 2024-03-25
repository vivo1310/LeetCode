class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            x = abs(x)
            if nums[x-1] < 0:
                res.append(x)
            nums[x-1] *= -1 # mark as visited
        return res
