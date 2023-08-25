class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for n in nums:
            if n not in hmap:
                hmap[n] = 1
            else:
                return True
        return False
        