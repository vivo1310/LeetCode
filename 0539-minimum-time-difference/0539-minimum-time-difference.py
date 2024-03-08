class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        best = 10**20
        N = len(timePoints)
        timePoints.sort() # to make sure min diff stay next to each other
        
        for i in range(N):
            hh, mm = timePoints[i].split(":")
            m1 = int(hh) * 60 + int(mm)
            
            hh, mm = timePoints[(i+1) % N].split(":")
            m2 = int(hh) * 60 + int(mm)
            
            best = min(abs(m2 - m1), 
                       abs(m2 + 60*24 - m1),
                       abs(m2 - (m1 + 60*24)),
                       best)
            # print(i,m1,m2,best)
        
        return best
        
            