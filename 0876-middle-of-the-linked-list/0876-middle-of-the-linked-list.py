# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        countPointer = head
        count = 0 # count number of node in this linked list
        while countPointer:
            countPointer = countPointer.next
            count += 1
        res = head
        for i in range(count // 2):
            res = res.next
        return res