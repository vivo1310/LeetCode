# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = ListNode()
        end = list1
        
        # set start to node a - 1 and end to node b
        for i in range(b):
            if i == a - 1:
                start = end # start to node a - 1
            end = end.next # end to node b
        
        start.next = list2
        
        while list2.next:
            list2 = list2.next
        
        list2.next = end.next
        end.next = None
        
        return list1
        
        
        