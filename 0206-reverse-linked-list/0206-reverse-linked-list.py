# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head.next == None:
        #     return head.val
        # return self.reverseList(head.next)
        # None <- 1 .. 2 -> 3 -> 4 -> 5 -> None
        
        prev = None
        curr = head
        while curr != None:
            nextNode = curr.next # 2 -> 3 ...
            curr.next = prev # swap
            prev = curr
            curr = nextNode
        return prev
        