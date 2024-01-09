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
                # i = 1
                while n+length in nSet:
                    length += 1
                    # i += 1
                # if length >= longestLength: longestLength = length
                longestLength = max(length, longestLength) #shorter than the aboe line
            
        return longestLength
    