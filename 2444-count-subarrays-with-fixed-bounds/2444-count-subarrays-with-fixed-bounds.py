class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minK_index = -1
        maxK_index = -1
        bad_index = -1
        res = 0
        # print('----',nums,'---------')
        for i, x in enumerate(nums):
            if x == minK:
                minK_index = i
            if x == maxK:
                maxK_index = i
            if x > maxK or x < minK:
                bad_index = i
            # print(minK_index, maxK_index, bad_index, max(0, min(minK_index, maxK_index) - bad_index))
            res += max(0, min(minK_index, maxK_index) - bad_index)
        return res