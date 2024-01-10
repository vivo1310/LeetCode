class Solution:
    def isPalindrome(self, s: str) -> bool:
        # .isalnum() check if a character is alphanumeric
        # set 2 pointers, 1 at the start, 1 at the end of the string
        # if the char at the pointer index is a alphanumeric char 
        # if 2 char is the same, move to the next index, repeat checking til 2 pointers meet
        # string = ''
        # # remove all non-alphanum char from - memory O(n) n is length of str
        # for c in s.lower():
        #     if c.isalnum():
        #         string += c
        # i = 0
        # j = len(string) - 1
        # while i < j:
        #     if string[i] != string[j]: 
        #         return False
        #     i += 1
        #     j -= 1
        # return True
    
    
        i = 0
        j = len(s) - 1
        while i < j:
            firstAlnumCheck = s[i].isalnum()
            secondAlnumCheck = s[j].isalnum()
            if firstAlnumCheck and secondAlnumCheck:
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
            elif not firstAlnumCheck:
                i += 1
            elif not secondAlnumCheck:
                j -= 1
        return True
        