class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [[1,2],[3,5],[6,7],[8,10],[12,16]]
        # [4,8]
        
        # 1. current interval < newInterval with no overlapping (eg. [1,2])
        # 2. current interval overlapping w newInterval
        # 3. newInterval < current interval with no overlapping (eg. [12,16])
        res = []
        n = len(intervals)
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < n and intervals[i][1] >= newInterval[0] and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)
        
        while i < n:
            res.append(intervals[i])
            i += 1
        # for i in intervals:
        #     if i[1] < newInterval[0] or i[0] > newInterval[1]: # case 1 and 3
        #         res.append(i)
        #     # elif i[0] > newInterval[1]: # case 3.
        #     #     res.append(i)
        #     else:
        #         newInterval[0] = min(i[0], newInterval[0])
        #         newInterval[1] = max(i[1], newInterval[1])
            
        # print(newInterval)
        # print(res)
        return res