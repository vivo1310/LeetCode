class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # square then sort O(nlogn)
        # sq = []
        # for n in nums:
        #     sq.append(n**2)
        # return sq
    
        # 2 pointers, start, end of nums
        # nums is non-decreasing
        # add max
        l, r = 0, len(nums) - 1
        res = []
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l]**2)
                l += 1
            else:
                res.append(nums[r]**2)
                r -= 1
        return res[::-1]