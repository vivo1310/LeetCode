class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxN = max(nums)
        # print(maxN)
        maxInWindow = 0
        i=0
        count = 0
        for j, x in enumerate(nums):
            if nums[j] == maxN:
                maxInWindow += 1
            while maxInWindow == k:
                if nums[i] == maxN:
                    maxInWindow -= 1
                i += 1
            count += i
        return count