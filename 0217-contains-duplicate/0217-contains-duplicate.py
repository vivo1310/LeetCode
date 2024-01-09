class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hmap = {}
        # for n in nums:
        #     if n not in hmap:
        #         hmap[n] = 1
        #     else:
        #         return True
        # return False
#       another way is to use hashset
        hashset = set()
        for n in nums:
            if n in hashset: # number is already existed in the hashset
                return True
            hashset.add(n)
        return False