class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0
        current_sum = 0
        # {prefix: number of occurrence}
        freq = {}  # To store the frequency of prefix sums

        for num in nums:
            current_sum += num
            if current_sum == goal:
                total_count += 1

            # Check if there is any prefix sum that can be subtracted from the current sum to get the desired goal
            if current_sum - goal in freq:
                total_count += freq[current_sum - goal]

            freq[current_sum] = freq.get(current_sum, 0) + 1

        return total_count

#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         return self.sliding_window_at_most(nums, goal) - self.sliding_window_at_most(nums, goal - 1)
#         count = 0
#         i = 0
#         while i < len(nums):
#             j = i + 1
#             currSum = sum(nums[i:j])
            
#             while currSum <= goal and j <= len(nums):
#                 if currSum == goal:
#                     count += 1
#                 # currSum = currSum + nums[j-1]
#                 # print(i,j,sum(nums[i:j+1+1]), currSum)
#                 # currSum = currSum + nums[j]
#                 print('old',i,j,currSum)
#                 currSum = currSum + nums[j-1]

#                 j += 1
#                 # currSum = sum(nums[i:j])
#                 print('new',i,j,currSum)
#             i += 1
#         return count