class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for n in nums:
            if n not in hashMap:
                hashMap[n] = 1
            else:
                hashMap[n] += 1
            if hashMap[n] > len(nums) / 2:
                return n
        return -1
        