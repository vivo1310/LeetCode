class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Method 1
        # subsets = [[], [nums[0]]]
        # i = 1
        # while i < len(nums):
        #     temp = []
        #     for element in subsets:
        #         temp.append(element) # dont include
        #         temp.append(element + [nums[i]]) # include
        #     subsets = temp
        #     i += 1
        # return subsets
    
    #     include 1?
    #         yes.[1]                                   no.[]
    #         |         \                             /        \
    #     include 2?                                 /          \
    #         |           \                         /            \
    #     yes.[1,2]        no.[1]               yes.[2]            no.[]
    #     include 3?          |     \             |     \           |    \
    #         |    \          |      \            |      \          |     \
    # yes.[1,2,3]  no.[1]   yes.[1,3] no.[1]   yes.[2,3] no.[2]    yes.[3] no.[]
    
        # Method 2: backtracking
        res = []
        subset = []

        def backtrack(i = 0):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include
            subset.append(nums[i])
            backtrack(i + 1)

            # decision not to include
            subset.pop()
            backtrack(i+1)

        backtrack()
        return res