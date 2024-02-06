class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[], [nums[0]]]
        i = 1
        while i < len(nums):
            temp = []
            for element in subsets:
                temp.append(element) # dont include
                temp.append(element + [nums[i]]) # include
            subsets = temp
            i += 1
        return subsets