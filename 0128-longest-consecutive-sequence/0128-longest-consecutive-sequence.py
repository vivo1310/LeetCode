class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # time: O(n), space: O(n) for the set
        longestLength = 0
        if not nums: return longestLength

        nSet = set(nums)
#       loop thru nums, check if n is the start of the sequence
#       if yes, check for next consecutive, until no more
#       if no, skip
        for n in nSet:
            length = 0
            if n-1 not in nSet: # it is the start of the sequence
                length += 1
                i = 1
                # print(n, length)
                while n+i in nSet:
                    length += 1
                    i += 1
                    # print(n, length)

                if length >= longestLength: longestLength = length
        # print(longestLength)
            
        return longestLength
        # if not nums: return 0
        # # create the map
        # hashMap = {} # n : n+1
        # for n in nums:
        #     hashMap[n] = n+1
        # # check for consecutive element
        # length = 1 # there's always a min length of 1 if there's a number in nums array
        # print(hashMap)
        # for k in hashMap:
        #     if hashMap[k] in hashMap.keys():
        #         print(k, hashMap[k])
        #         length += 1
        # return length