class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1
        
        while i < j:
            if len(s) == 1:
                return 1
            if s[i] == s[j]:
                # print(i,j)
                while i+1<len(s) and s[i+1] == s[i]:
                    # print('yes',i,j)
                    i += 1
                while j-1>0 and s[j-1] == s[j]:
                    j -= 1
                s = s[i+1:j]
                i, j = 0, len(s) - 1
            else:
                return len(s)
            # print(s)
        return len(s)
            
#         #cabaabac 8
#         def getPrefixInd(s):
#             pref = s[0]
#             for i in range(1, len(s)):
#                 if pref[0] == s[i]:
#                     pref = s[:i+1]
#                 else:
#                     return [pref,i]
#             return None
#         def getSuffixInd(s):
#             suff = s[len(s) - 1]
#             for j in range(1, len(s)):
#                 if suff[0] == s[-j]:
#                     suff = s[-j:]
#                 else:
#                     return [suff,len(s) - j + 1]
#             return None
#                     # break
#             # return [suff,len(s) - j + 1]
        
#         [pre,i] = getPrefixInd(s)
#         [suf,j] = getSuffixInd(s)
#         print('first', pre, i, suf, j)
#         while pre[0] == suf[0]:
#             s = s[i:j]
#             [pre,i] = getPrefixInd(s)
#             [suf,j] = getSuffixInd(s)
#             print(s, pre, i, suf, j)
#         return len(s)
            
            
        # for j in range(len(s) - 2, -1, -1):
        #     if suff[0] == s[j]:
        #         print(j, s[len(s) - 1:j - 1:-1],'aa')
        #         suff = s[len(s) - 1:j - 1:-1
        #     else:
        #         break
        # while prefix == suffix:
        #     i += 1
        #     prefix = prefix[:i+1]
        # while prefix == suffix:
        #     j -= 1
        #     suffix = suffix[j:j-1:-1]
        # print(prefix, suffix)
#             if i == j:
#                 return 0 if s[i] == prev else 1
                
#             print(i, j, s[i],s[j],s)
#             if s[i] == s[j]:
#                 prev = s[i]
#                 s = s[i + 1:j]
#                 print('11',s)
#             elif s[i] == prev:
#                 s = s[i + 1:j+1]
#                 print('22',s)
                
#             elif s[j] == prev:
#                 s = s[i:j]
#                 print('33',s)
                
#             else:
#                 print('44',s)
                
#                 return len(s)
#             # i = 0
#             j = len(s) - 1
#         return len(s)