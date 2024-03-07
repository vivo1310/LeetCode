# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1st method: Traverse once to count number of nodes in the list
        # countPointer = head
        # count = 0 # count number of node in this linked list
        # while countPointer:
        #     countPointer = countPointer.next
        #     count += 1
        # res = head
        # for i in range(count // 2):
        #     res = res.next
        # return res
        
        # 2nd method: Slow 1 step, fast 2 steps pointer
        # Slow will point to middle when fast reach the end
        
        slow, fast = head, head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow