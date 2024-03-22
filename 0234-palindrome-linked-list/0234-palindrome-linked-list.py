# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #convert to list
        ls = []
        cur = head
        while cur:
            ls.append(cur.val)
            if cur.next:
                cur = cur.next
            else:
                break
        
        #check if list is palindrom
        i,j = 0, len(ls) - 1
        while i < j:
            if ls[i] != ls[j]:
                return False
            i += 1
            j -= 1
        return True
        