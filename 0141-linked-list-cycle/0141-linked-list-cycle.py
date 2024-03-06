# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's cycle finding algo
        # 2 pointer, 1 go 1 step, another one go 2 step at a time
        # move pointers til pointer 1 reach the end
        # if there's cycle, pointer 1 and 2 must meet somewhere before the loop end
        # slow, fast = head, head
        # while slow and fast and fast.next:
        #     slow = slow.next # 1 step forward
        #     fast = fast.next.next # 2 step at a time
        #     if slow == fast:
        #         return True
        # return False
    
        # Using Hash table
        # hashSet = set()
        # temp = head
        # while temp:
        #     if temp in hashSet:
        #         return True
        #     hashSet.add(temp)
        #     temp = temp.next
        # return False
    
        slow, fast = head, head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
        
        