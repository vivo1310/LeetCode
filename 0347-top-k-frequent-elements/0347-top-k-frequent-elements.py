class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # top k -> should involve sort or heap
        # Counter nums, sort values of the counter hashmap
        
        numToFreq = Counter(nums) # num -> freq
        
        freqToNums = collections.defaultdict(list) # freq -> list of num # {1: [1,2], 2: [3]}

        for num, freq in numToFreq.items():
            freqToNums[freq].append(num)
        
        maxHeap = [-x for x in freqToNums.keys()]
        heapq.heapify(maxHeap)
        
        res = []
        while k > 0:
            top = -heapq.heappop(maxHeap)
            for n in freqToNums[top]:
                res.append(n)
                k -= 1
        
        return res