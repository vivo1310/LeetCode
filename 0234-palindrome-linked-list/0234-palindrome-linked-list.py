# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         #convert to list
#         ls = []
#         cur = head
#         while cur:
#             ls.append(cur.val)
#             if cur.next:
#                 cur = cur.next
#             else:
#                 break
        
#         #check if list is palindrom
#         i,j = 0, len(ls) - 1
#         while i < j:
#             if ls[i] != ls[j]:
#                 return False
#             i += 1
#             j -= 1
#         return True
        
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: # O(n) time, O(n/2) space
        def reverse(head):
            prevNode = None
            currNode = head
            while currNode:
                nextNode = currNode.next
                currNode.next = prevNode
                prevNode = currNode
                currNode = nextNode
            return prevNode
        
        # move slow pointer to middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half of linked list
        reversedHalf = reverse(slow)
        while reversedHalf:
            if head.val != reversedHalf.val:
                return False
            head = head.next
            reversedHalf = reversedHalf.next
        return True