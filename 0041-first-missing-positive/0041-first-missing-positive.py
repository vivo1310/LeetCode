class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # cycle sort (for place number in correct order following range [1,n]])
        n = len(nums)
        # 3,4,-1,1
        i = 0
        while i < n:
            correctInd = nums[i] - 1 # if nums[i] is 3, then its correct index should be 2
            if 0 < nums[i] <= n and nums[i] != nums[correctInd]:
                # swap 
                nums[i], nums[correctInd] = nums[correctInd], nums[i]
            else:
                i += 1
        
        # nums now should be[1,2,3,4,5]
        for i in range(n):
            if nums[i] != i + 1: # the number is not in the correct position
                return i + 1
        
        # if all num are in the correct position
        # the smallest missing positive num should be n+1
        return n + 1
            