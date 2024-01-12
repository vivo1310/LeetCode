# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive O(n) memory O(n) cuz creating newHead
        if not head:
            return head
        newHead = head
        if head.next: # if we still have sub-problem
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
    
    
        # Iterative time O(n) memory O(1) cuz using 2 pointer
        # None <- 1  ..  2 -> 3 -> 4 -> 5 -> None
        # prev = None
        # curr = head
        # while curr != None:
        #     nextNode = curr.next # 2 -> 3 ...
        #     curr.next = prev # swap
        #     prev = curr
        #     curr = nextNode
        # return prev
        