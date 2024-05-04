class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit: j -= 1
            i += 1
        return i
#         res = []
        
#         P = sorted(people)
#         print(sP)
        
#         curr = 0
#         gr = []
#         for n in P:
#             if curr + n <= limit:
#                 gr.append(n)
#                 curr += n
            
                
        
#         return len(res)