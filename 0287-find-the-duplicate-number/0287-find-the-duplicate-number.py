class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1.hashset - extra space
        # 2.linked list cycle
        for i in range(len(nums)):
            ind = abs(nums[i])
            # print(i,ind)

            if nums[ind] < 0:
                return ind
            nums[ind] = -nums[ind]
            # print(nums)
        return -1