# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1-2-3-4-5-6-7-8->None , n = 4
        slow, fast = head, head
        # start moving fast n step
        # then assign slow so that the 2 pointers are n-step apart
        
        for _ in range(n):
            fast = fast.next
        
        if not fast: return slow.next # edge case
        
        while fast.next: # start moving 2 pointers which are n-step apart
            fast = fast.next
            slow = slow.next
        
        # remove node
        slow.next = slow.next.next
        
        return head
    
        
        
        