class Solution:
    def isValid(self, s: str) -> bool:
        # time and space O(n)
        hashMap = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        stack = []
        
        for c in s:
            if c in hashMap: # check if char is an open bracket
                stack.append(c)
            else:
                if stack == []:
                    return False
                last = stack.pop()
                if c != hashMap[last]:
                    return False
        if stack == []: return True
        return False
        # return True