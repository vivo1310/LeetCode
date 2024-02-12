class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time: O(n), space: O(n)
        # map = {}
        # for i, n in enumerate(nums):
        #     find = target - n
        #     if find in map:
        #         return [map[find],i]
        #     map[n] = i

        # use enumerate to get the index and the value of the array's item
        hashMap = {}  # val:index
        for i, n in enumerate(nums):
            m = target - n
            if m in hashMap:
                return [
                    hashMap[m],
                    i,
                ]  # i is current index, hashMap[m] is index of m in nums array
            hashMap[n] = i
