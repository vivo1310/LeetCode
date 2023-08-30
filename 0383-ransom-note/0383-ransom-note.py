from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         m = {} # magazine letter occurence
#         for c in magazine:
#             if c not in m:
#                 m[c] = 1
#             else:
#                 m[c] += 1
#         n = {} # ransomNote letter occurence
#         for c in ransomNote:
#             if c not in n:
#                 n[c] = 1
#             else:
#                 n[c] += 1
# #         loop thru m, check occ of each letter is the same in ransomNote occ
#         for l in n.keys():
#             if m.get(l) is None or m[l] < n[l]:
#                 return False
#         return True
        m = Counter(magazine)
        rn = Counter(ransomNote)
        for i in rn:
            if i not in m or m[i] < rn[i]:
                return False
            
        return True