class Solution:
    def minimumLength(self, s: str) -> int:
        # using queue
        q = collections.deque(s)
        
        while len(q) > 1 and q[0] == q[-1]:
            c = q[0]
            
            while len(q) > 0 and q[0] == c:
                q.popleft()
            while len(q) > 0 and q[-1] == c:
                q.pop()
            
        return len(q)
    
        # 2 pointers
        # i, j = 0, len(s) - 1
        # while i < j and s[i] == s[j]:
        #     c = s[i] # character of similar prefix
        #     while i <= j and s[i] == c:
        #         i += 1
        #     while j > i and s[j] == c:
        #         j -= 1
        # return j - i + 1
    
        # first approach, old code
        # while i < j:
        #     if s[i] == s[j]:
        #         while i + 1 < len(s) and s[i +1 ] == s[i]:
        #             i += 1
        #         while j - 1 > 0 and s[j-1] == s[j]:
        #             j -= 1
        #         s = s[i + 1:j]
        #         i, j = 0, len(s) - 1
        #     else:
        #         return len(s)
        # return len(s)