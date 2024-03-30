class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarraysWithAtMostK(nums, k):
            f = Counter()
            i = 0
            count = 0
            for j, x in enumerate(nums):
                f[x] += 1
                while len(f) > k:
                    f[nums[i]] -= 1
                    if f[nums[i]] == 0:
                        del f[nums[i]]
                    i += 1
                count += j - i + 1 # explain below:
                # array of length x - num of subarrays
                # 1,3,6,10,15
                # (count = count + length)
                # arr of length 1 has 1 subarr (0 + 1)
                # arr of length 2 has 3 subarr (1 + 2)
                # arr of length 3 has 6 subarr (3 + 3)
                # arr of length 4 has 10 subarr (6 + 4)
                # arr of length 5 has 15 subarr (10 + 5)

            return count
        # subarr with exact k distinct = subarr with at most k - subarr with at most k-1
        return subarraysWithAtMostK(nums,k) - subarraysWithAtMostK(nums,k-1)