class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        res = 0
        score = nums[0] + nums[1]

        while len(nums) >= 2:
            currScore = nums[0] + nums[1]
            if currScore == score:
                nums = nums[2:]
                res += 1
            else:
                break

        return res
    
        