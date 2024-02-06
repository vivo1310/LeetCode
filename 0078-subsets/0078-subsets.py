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
    
    #     include 1?
    #         yes.[1]                                   no.[]
    #         |         \                             /        \
    #     include 2?                                 /          \
    #         |           \                         /            \
    #     yes.[1,2]        no.[1]               yes.[2]            no.[]
    #     include 3?          |     \             |     \           |    \
    #         |    \          |      \            |      \          |     \
    # yes.[1,2,3]  no.[1]   yes.[1,3] no.[1]   yes.[2,3] no.[2]    yes.[3] no.[]