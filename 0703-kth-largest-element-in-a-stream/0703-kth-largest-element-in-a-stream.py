# class KthLargest: # using sort 

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = nums
        

#     def add(self, val: int) -> int: # O(nlogn) due to sorting
#         self.nums.append(val)
#         self.nums.sort()
#         return self.nums[len(self.nums) - self.k]

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.nums = nums
    

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)